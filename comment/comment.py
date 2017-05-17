#!/usr/bin/python
#coding=utf-8

import codecs
try:
	import sys
	reload(sys)
	sys.setdefaultencoding('utf8')
except:
	pass
import copy
if __name__ != '__main__':
	from rules import _loader as loader
	RULES = loader.load_rules()
else:
	RULES = {}

DEFAULT_CHAR = u'/'

def xor(a, b):
	return bool(a) != bool(b)

FIELDS = [
'userProvince','userLevelName','price','userClientShow','creationTime','orderProcessSpeed',
'shipSpeed','deliverySpeed','isOnTimeDelivery','isDeliveryCorrect','isDeliveryIntact',
'isDifficultLastMile','isDeliveryLastMile','deliveryServiceAttitude','installerArrivalTime',
'installerArrivalSpeed','installSpeed','installResult','installerExplain','installerAttitude',
'isInstallerArbitraryCharges','isBillComplete','isGiftPresentation','isAfterSale','isReturnVisit',
'isGiftByAfterSale','isConnectCustomerService','connectCustomerServiceReason','customerServiceEffectiveness',
'isMaintain','maintainTimes','maintainResult','isReplacement','replacementResult','replacementTimes',
'isReturn','returnResult','retrunTimes','afterSaleEffectiveness','afterSaleAttitude','isDemandResolved',
'referenceName','isPriceChange','priceChanged','priceCompare','priceDifference','functionalDiversity',
'energyEfficiency','performance','noiseFigure','beautiful','complete','isBreakdown','failureIndex',
'EaseOfUse','brandAwareness','productAwareness','sftOfCostEffective','sftOfInsured','sftOfOrderProcess',
'sftOfDelivery','sftOfInstallation','sftOfAfterSale','sftOfProductQuality','sftOfProductConsistent',
'sftOfPrepurchaseExpectation','score','sftLevel','compilation','willOfRepurchasecategory','willOfRepurchaseBand',
'recommended','plusAvailable','isMobile','userLevelId','userClient','commentTime','referenceTime','days','content','keywords']

OUT_HEADERS = [
	'id','Order_from','Comment_time','Order_processing_speed','Sending_out_speed',
	'Delivery_speed','If_delivered_on_original/promised_date','If_delivered_right_product',
	'If intact in transit','If the last Km is difficult','If the last Km is served',
	'Distribution staff service attitude','Installer arrival time','Installer arrival speed',
	'Installation speed','Installation effect','Explaining service','Installer service attitude',
	'If installer has any charges','If the bill is complete',
	'If any gifts','If any after-sales processes','If any revisiting',
	'If any gifts from after-sales','If contacted customer service',
	'Reason contacting customer service','Customer service processing efficiency',
	'If fixing','Number of fixing','Fixing result','If replacement','Replacement result',
	'If return','Return result','After-sales processing efficiency','After-sales attitude',
	'If problems solved','Product model','If price changed in a short time','Changing price',
	'Compared to different channel prices','Price gap','Product functional diversity',
	'Energy saving index','Performance index','Noise situation','Aesthetics performance',
	'Intactness performance','If product is faulty','Fault index','Ease of use',
	'Cost-effective satisfaction','Reputation and price satisfaction','Order processing satisfaction',
	'Logistics distribution satisfaction','Installation satisfaction','After-sales service satisfaction',
	'Product quality satisfaction','User_region','User_level','User_purchase_amount',
	'Consistent with the description satisfaction','Compared with pre-purchase expectations satisfaction',
	'Customer satisfaction','Customer satisfaction level','Customer complaints index',
	'Brand awareness to Haier','Awareness to product',
	'Will of repurchase the same brand and the same kind of product',
	'Will of repurchase the same brand','Recommended to buy index']

OUT_ORDERS = [
	None, 'userClientShow', 'creationTime', 'orderProcessSpeed', 'shipSpeed',
	'deliverySpeed', 'isOnTimeDelivery', 'isDeliveryCorrect', 'isDeliveryIntact', 'isDifficultLastMile',
	'isDeliveryLastMile', 'deliveryServiceAttitude', 'installerArrivalTime',
	'installerArrivalSpeed','installSpeed','installResult','installerExplain',
	'installerAttitude', 'isInstallerArbitraryCharges', 'isBillComplete',
	'isGiftPresentation','isAfterSale','isReturnVisit','isGiftByAfterSale',
	'isConnectCustomerService','connectCustomerServiceReason','customerServiceEffectiveness',
	'isMaintain','maintainTimes','maintainResult','isReplacement','replacementResult',
	'isReturn','returnResult','afterSaleEffectiveness','afterSaleAttitude',
	'isDemandResolved','referenceName','isPriceChange','priceChanged','priceCompare',
	'priceDifference','functionalDiversity','energyEfficiency','performance','noiseFigure',
	'beautiful','complete','isBreakdown','failureIndex','EaseOfUse','sftOfCostEffective',
	'sftOfInsured','sftOfOrderProcess','sftOfDelivery','sftOfInstallation','sftOfAfterSale',
	'sftOfProductQuality','userProvince','userLevelName','price','sftOfProductConsistent',
	'sftOfPrepurchaseExpectation','score','sftLevel','compilation','brandAwareness',
	'productAwareness','willOfRepurchasecategory','willOfRepurchaseBand','recommended']

DEFAILT_VALUE = {
'userProvince': DEFAULT_CHAR, 'userLevelName': DEFAULT_CHAR,'price': 0,'userClientShow': u'来自网页购物','creationTime': u'',
'orderProcessSpeed': 3,'shipSpeed': 3,'deliverySpeed': 3,'isOnTimeDelivery': True,'isDeliveryCorrect': True,'isDeliveryIntact': True,
'isDifficultLastMile': False,'isDeliveryLastMile': True,'deliveryServiceAttitude': 3,'installerArrivalTime': u'配送员安装',
'installerArrivalSpeed': 3,'installSpeed': 3,'installResult': 3,'installerExplain': 3,'installerAttitude': 3,'isInstallerArbitraryCharges': False,
'isBillComplete': True,'isGiftPresentation': False,'isAfterSale': False,'isReturnVisit': False,'isGiftByAfterSale': False,'isConnectCustomerService': False,
'connectCustomerServiceReason': DEFAULT_CHAR,'customerServiceEffectiveness': 3,'isMaintain': False,'maintainTimes': DEFAULT_CHAR,'maintainResult': DEFAULT_CHAR,
'isReplacement': False,'replacementResult': DEFAULT_CHAR,'replacementTimes': DEFAULT_CHAR,'isReturn': False,'returnResult': DEFAULT_CHAR,
'retrunTimes': DEFAULT_CHAR,'afterSaleEffectiveness': 3,'afterSaleAttitude': 3,'isDemandResolved': True,'referenceName': u'','isPriceChange': False,
'priceChanged': DEFAULT_CHAR,'priceCompare': False,'priceDifference': DEFAULT_CHAR,'functionalDiversity': 3,'energyEfficiency': 3,'performance': 3,
'noiseFigure': 3,'beautiful': 3,'complete': 3,'isBreakdown': False,'failureIndex': DEFAULT_CHAR,'EaseOfUse': 3,'brandAwareness': 3,'productAwareness': 3,

#satisfactionOf
'sftOfCostEffective': 3,'sftOfInsured': 3,'sftOfOrderProcess': 3,'sftOfDelivery': 3,'sftOfInstallation': 3,'sftOfAfterSale': 3,'sftOfProductQuality': 3,
'sftOfProductConsistent': 3,'sftOfPrepurchaseExpectation': 3,'score': 0,'sftLevel': u'','compilation': 0,'willOfRepurchasecategory': 3,'willOfRepurchaseBand': 3,
'recommended': 3,

#extern
'plusAvailable': 0,'isMobile': 0,'userLevelId': u'','userClient': 0,'commentTime': u'','referenceTime': u'','days': 0,'content': u'','keywords': u''
}


class Comment(object):
	def __init__(self):
		self.data = copy.deepcopy(DEFAILT_VALUE)

	def __checkUserLevelName(self):
		return True

	def __checkUserClientShow(self):
		return True

	def __checkOrderDelivery(self):
		return True

	def __checkInstallation(self):
		return True

	def __checkCustomerService(self):
		if self.data['isConnectCustomerService'] and not self.data['isAfterSale']:
			return False
		if not xor(self.data['isAfterSale'], self.data['sftOfAfterSale'] == DEFAULT_CHAR):
			return False
		if not self.data['isAfterSale']:
			return self.data['afterSaleEffectiveness'] != DEFAULT_CHAR \
				and self.data['afterSaleAttitude'] != DEFAULT_CHAR \
				and self.data['isDemandResolved'] != DEFAULT_CHAR
		else:
			return self.data['afterSaleEffectiveness'] == DEFAULT_CHAR \
				and self.data['afterSaleAttitude'] == DEFAULT_CHAR \
				and self.data['isDemandResolved'] == DEFAULT_CHAR

	def __checkPrice(self):
		return xor(self.data['isPriceChange'], self.data['priceChanged'] == DEFAULT_CHAR) \
			and xor(self.data['priceCompare'], self.data['priceDifference'] == DEFAULT_CHAR)

	def __checkBreakdown(self):
		return xor(self.data['isBreakdown'], self.data['failureIndex'] == DEFAULT_CHAR)

	def check(self):
		return self.__checkUserLevelName() and self.__checkUserClientShow() \
			and self.__checkOrderDelivery() and self.__checkInstallation() \
			and self.__checkCustomerService() and self.__checkPrice() \
			and self.__checkBreakdown()

	def getSftLevel(self, score):
		if score > 3:
			return '好评'
		elif score > 1:
			return '中评'
		else:
			return '差评'

	def fill(self, comment):
		if comment['userProvince'] != '':
			self.data['userProvince'] = comment['userProvince']
		if comment['userClientShow'] != '':
			self.data['userClientShow'] = comment['userClientShow']
		self.data['userLevelName'] = comment['userLevelName']
		self.data['creationTime'] = comment['creationTime']
		self.data['plusAvailable'] = comment['plusAvailable']
		self.data['referenceName'] = comment['referenceName']
		self.data['referenceTime'] = comment['referenceTime']
		self.data['userLevelId'] = comment['userLevelId']
		self.data['userClient'] = comment['userClient']
		self.data['score'] = comment['score']
		self.data['sftLevel'] = self.getSftLevel(int(comment['score']))
		self.data['isMobile'] = comment['isMobile']
		self.data['days'] = comment['days']
		self.data['content'] = '"{0}"'.format(comment['content'])
		self.data['keywords'] = '"{0}"'.format(comment['keywords'])

	def matchRule(self, field, rules, keywords):
		for rule in rules:
			if set(rule[1:]).issubset(keywords):
				self.data[field] = rule[0]

	def matchRules(self, keywords):
		for field in FIELDS:
			if field in RULES.keys():
				self.matchRule(field, RULES[field], set(keywords))

	def __str__(self):
		data = []
		for field in OUT_ORDERS:
			if field != None:
				data.append(self.data[field])
			else:
				data.append('None')
		return ','.join(''.join(str(elems)) for elems in data)

for field in FIELDS:
	if not field in DEFAILT_VALUE:
		raise Exception

for key in RULES.keys():
	if not field in DEFAILT_VALUE:
		raise Exception

if __name__ == '__main__':
	comment = Comment()
	with codecs.open('test.csv', 'w', 'gb2312') as f:
		f.write((','.join(OUT_HEADERS) + '\n').decode('utf-8'))
		print(','.join(OUT_HEADERS))
		f.write((str(comment) + '\n').decode('utf-8'))
		print(str(comment))

