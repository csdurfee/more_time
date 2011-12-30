# views used on the admin side.

from view_imports import *
import pprint

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/redis_debug')
def redis_debug():
	RANGE_SIZE = 100
	try:
		offset = request.values['offset']
	except:
		offset = 0
	try:
		philtre = request.values['filter']
	except:
		philtre = "*"
	client = g.redisco_client
	all_keys = client.keys(philtre)
	kir = all_keys[offset:offset+RANGE_SIZE]

	results_in_range = dict(zip(kir, client.mget(kir)))

	ctx = dict(
		db_size = client.dbsize(),
		results_in_range = results_in_range,
	)
	resp = make_response(pprint.pformat(ctx))

	return resp