from graphql_client import GraphQLClient

ws = GraphQLClient('ws://localhost:8000/graphql')
query = """
query{
{
  allPosts{
    edges{
      node{
        title
        body
        author{
          username
        }
      }
    }
  }
}
}  
"""
res = ws.query(query)
print(res)
ws.close()
