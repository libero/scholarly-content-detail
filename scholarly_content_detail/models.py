from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# Many to Many relationship between a Category and Article
cat_article_m2m = db.Table('cat_article_m2m',
    db.Column('category_id', db.String(255), db.ForeignKey('categories.id')),
    db.Column('article_id', db.String(255), db.ForeignKey('articles.id'))
)


class Category(db.Model):
    """This class represents the categories table."""

    __tablename__ = 'categories'

    id = db.Column(db.String(255), primary_key=True, autoincrement=False)
    name = db.Column(db.String(255))
    articles = db.relationship(
        'Article',
        secondary=cat_article_m2m,
        back_populates='categories'
    )

    def add_articles_by_id(self, article_ids):
        articles = Article.query.filter(Article.id.in_(article_ids)).all()
        self.articles.extend(articles)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Category \'%s\': %s>' % (self.id, self.name)


class Article(db.Model):
    """This class represents the articles table."""

    __tablename__ = 'articles'

    id = db.Column(db.String(255), primary_key=True, autoincrement=False)
    categories = db.relationship(
        Category,
        secondary=cat_article_m2m,
        back_populates='articles'
    )

    def add_categories_by_id(self, category_ids):
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        self.categories.extend(categories)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<Article \'%s>\'' % self.id
