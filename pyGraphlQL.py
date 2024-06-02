import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Book:
    title: str
    author: str
    price: int

@strawberry.type
class Query:
    @strawberry.field
    def book(self) -> Book:
        return Book(title="Computer Fundamentals", author="Sinha", price=300)

schema = strawberry.Schema(query=Query)

graphql_app = GraphQLRouter(schema)

app = FastAPI()

# Include the GraphQL router at the "/graphql" endpoint
app.include_router(graphql_app, prefix="/graphql")

# You don't need to add route or websocket_route separately
# app.add_route("/book", graphql_app)
# app.add_websocket_route("/book", graphql_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
