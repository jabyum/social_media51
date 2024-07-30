from database.models import *
from database import get_db
from datetime import datetime


#  получить информацию о всех или об одном посте
def get_all_or_exact_post_db(post_id):
    with next(get_db()) as db:
        if post_id == 0:
            all_posts = db.query(UserPost).filter_by(id=post_id).all()
            return [[post.user_id, post.main_text, post.hashtag]for post in all_posts]
        else:
            post = db.query(UserPost).filter_by(id=post_id).first()
            return [post.user_id, post.main_text, post.hashtag]

# редактирование поста
def change_post_text(post_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(post_id=post_id).first()
    if exact_post:
        exact_post.main_text = new_text

        db.commit()
        return 'Успешно измененно'
    else:
        return False

# удаление поста
def delete_post_text(post_id):
    db = next(get_db())

    delete_post = db.query(UserPost).filter_by(id=post_id).first()

    if delete_post:
        # db.delete(delete_post_photo)
        # db.commit()

        db.delete(delete_post)
        db.commit()
        return 'Успешно удалено'
    else:
        return False

# публикация поста (регистрация поста)
def public_post_text(user_id, main_text, hashtag):
    db = next(get_db())
    new_post = UserPost(user_id=user_id, main_text=main_text, hashtag=hashtag, reg_date=datetime.now())
    db.add(new_post)
    db.commit()
    return 'Успешно добалено'

# добавление комментария
def public_comment_db(user_id, main_text, post_id,text):
    db = next(get_db())

    new_comments = UserPost(user_id=user_id, main_text=main_text, post_id=post_id,text=text, reg_date=datetime.now())

    db.add(new_comments)
    db.commit()
    return 'Успешно добалено'


# получение всех комментариев определенного поста
def get_exact_post_comments(post_id):
    db = next(get_db())
    exact_post = db.query(Comment).filter_by(post_id=post_id).all()
    return [[comment.user_id, comment.text] for comment in exact_post]

# изменение текста комментария
def change_comment_text_db(comment_id, new_text):
    db = next(get_db())

    exact_post = db.query(UserPost).filter_by(comment_id=comment_id).first()

    if exact_post:
        exact_post.text = new_text

        db.commit()
        return 'Успешно измененно'
    else:
        return False


# удаление комментария
def delete_exact_comment_db(comment_id):
    db = next(get_db())

    delete_post = db.query(Comment).filter_by(id=comment_id).first()

    if delete_post:
        db.delete(delete_post)
        db.commit()
        return 'Успешно удалено'
    else:
        return False


# создание хештега
def add_heshtag(name):
    db = next(get_db())

    new_post = UserPost(hashtag_name=name)

    db.add(new_post)
    db.commit()
    return 'Успешно добалено'

# поиск постов о хештеге
def get_some_hashtag_db(hashtag_name):
    db = next(get_db())
    posts = db.query(UserPost).filter_by(hashtag_name=hashtag_name).all()
    if posts:
        return [[post.user_id, post.main_text] for post in posts]