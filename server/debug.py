import ipdb
from app import app
from models import Game, db

if __name__ == '__main__':
    with app.test_request_context():
        ipdb.set_trace()
        game = Game.query.first()
        game_dict = game.to_dict()
        print(game_dict)

    app.run(debug=True)
