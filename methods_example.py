# in this section I'm going to simulate how the methods of and rest api behave 

def generate_id(start=1): 
    current_id = start
    while True: 
        yield current_id
        start += 1 


def find(posts, id): 
    return next((post for post in posts if post["id"] == id), None)

def replace(posts: list[dict],id: int,post: dict ): 
    for v in posts: 
        if id in v: 
            v[id] = post
                
            

# first we create a source 
posts = [
    {"id": generate_id, "title": "A"},
    {"id": generate_id, "title": "B"}
]

# the we have the first method that is get -> this just read the information 
def GET_all_posts(): 
    return posts

# the concept behid is the next: No mutation, just read 

# the next method is post that create new data inside 
def POST_new_posts(new_data): 
    new_id = generate_id()
    new_post = {"id": new_id, **new_data}
    posts.append(new_post)
    return new_post
 
 
# conceptually this just take the last state and add new information to it 

def PUT_post(id, new_data): 
    post = find(posts,id)
    post = {"id": id, **new_data}
    replace(posts,id,post)
    return post

# everything in the the source is overwritten 

# PATCH modify partially so it search only one element and change it 
def PATCH_posst(id, partial_data): 
    post = find(posts,id)
    
    if post is None: 
        return {"Error": "Post was not finded"}
    
    for key in partial_data: 
        if key in post: 
           post[key] = partial_data[key]
    return post   


# and delete remove the elements making this 
def DELETE_post(id): 
    post = find(posts,id)
    
    if posts: 
        posts.remove(post)
        return {"Message": "succesfully removed"}
    
    return {"Error": "post was not finded"}