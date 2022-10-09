from helpers import scrap_pool_results, uri_from_date, save_results_to_db
from flask import jsonify, request


def apply_views(app):
    @app.route('/api/v1/scrap-pools', methods=['POST'])
    def scrap_pools():
        date = request.form.get('date')
        uri = uri_from_date(date)
        results = scrap_pool_results(uri)
        save_results_to_db(results)
        response = {'message': 'success'}
        return jsonify(response)
