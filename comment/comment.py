#!/usr/bin/python
#coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

DEFAULT_CHAR = '/'

def xor(a, b):
	return bool(a) != bool(b)

class Comment(object):
	def __init__(self):
		self.userProvince = DEFAULT_CHAR
		self.userLevelName = u''
		self.price = 0
		self.userClientShow = u'来自网页购物'
		self.createTime = u''
#		self.commentTime = ''
#		self.days = 0
		self.orderProcessSpeed = 3
		self.shipSpeed = 3
		self.deliverySpeed = 3
		self.isOnTimeDelivery = True
		self.isDeliveryCorrect = True
		self.isDeliveryIntact = True
		self.isDifficultLastMile = False
		self.isDeliveryLastMile = True
		self.deliveryServiceAttitude = 3

		self.installerArrivalTime = u'配送员安装'
		self.installerArrivalSpeed = 3
		self.installSpeed = 3
		self.installResult = 3
		self.installerExplain = 3
		self.installerAttitude = 3
		self.isInstallerArbitraryCharges = False
		self.isBillComplete = True
		self.isGiftPresentation = False

		self.isAfterSale = False
		self.isReturnVisit = False
		self.isGiftByAfterSale = False
		self.isConnectCustomerService = False
		self.connectCustomerServiceReason = DEFAULT_CHAR
		self.customerServiceEffectiveness = 3
		self.isMaintain = False
		self.maintainTimes = DEFAULT_CHAR
		self.maintainResult = DEFAULT_CHAR
		self.isReplacement = False
		self.replacementResult = DEFAULT_CHAR
		self.replacementTimes = DEFAULT_CHAR
		self.isReturn = False
		self.returnResult = DEFAULT_CHAR
		self.retrunTimes = DEFAULT_CHAR
		self.afterSaleEffectiveness = 3
		self.afterSaleAttitude = 3
		self.isDemandResolved = True

		self.equipmentModel = u''

		self.isPriceChange = False
		self.priceChanged = DEFAULT_CHAR
		self.priceCompare = False
		self.priceDifference = DEFAULT_CHAR

		self.functionalDiversity = 3
		self.energyEfficiency = 3
		self.performance = 3
		self.noiseFigure = 3
		self.beautiful = 3
		self.complete = 3
		self.isBreakdown = False
		self.failureIndex = DEFAULT_CHAR
		self.EaseOfUse = 3

		self.brandAwareness = 3
		self.productAwareness = 3

		#satisfactionOf
		self.sftOfCostEffective = 3
		self.sftOfInsured = 3
		self.sftOfOrderProcess = 3
		self.sftOfDelivery = 3
		self.sftOfInstallation = 3
		self.sftOfAfterSale = 3
		self.sftOfProductQuality = 3
		self.sftOfProductConsistent = 3
		self.sftOfPrepurchaseExpectation = 3

		self.score = u''
		self.sftLevel = u''

		self.compilation = 1
		self.willOfRepurchasecategory = 3
		self.willOfRepurchaseBand = 3
		self.recommended = 3

	def checkUserLevelName(self):
		return True

	def checkUserClientShow(self):
		return True

	def checkOrderDelivery(self):
		return True

	def checkInstallation(self):
		return True

	def checkCustomerService(self):
		if self.isConnectCustomerService and not self.isAfterSale:
			return False
		if not xor(self.isAfterSale, self.sftOfAfterSale == DEFAULT_CHAR):
			return False
		if not self.isAfterSale:
			return self.afterSaleEffectiveness != DEFAULT_CHAR \
				and self.afterSaleAttitude != DEFAULT_CHAR \
				and self.isDemandResolved != DEFAULT_CHAR
		else:
			return self.afterSaleEffectiveness == DEFAULT_CHAR \
                and self.afterSaleAttitude == DEFAULT_CHAR \
                and self.isDemandResolved == DEFAULT_CHAR

	def checkPrice(self):
		return xor(self.isPriceChange, self.priceChanged == DEFAULT_CHAR) \
			and xor(self.priceCompare, self.priceDifference == DEFAULT_CHAR)

	def checkBreakdown(self):
		return xor(self.isBreakdown, self.failureIndex == DEFAULT_CHAR)

	def check(self):
		return self.checkUserLevelName() and self.checkUserClientShow() \
			and self.checkOrderDelivery() and self.checkInstallation() \
			and self.checkCustomerService() and self.checkPrice() \
			and self.checkBreakdown()

	def __str__(self):
		return u'"{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}",' \
			'"{10}","{11}","{12}","{13}","{14}","{15}","{16}","{17}","{18}","{19}",' \
			'"{20}","{21}","{22}","{23}","{24}","{25}","{26}","{27}","{28}","{29}",' \
			'"{30}","{31}","{32}","{33}","{34}","{35}","{36}","{37}","{38}","{39}",' \
			'"{40}","{41}","{42}","{43}","{44}","{45}","{46}","{47}","{48}","{49}",' \
			'"{50}","{51}","{52}","{53}","{54}","{55}","{56}","{57}","{58}","{59}",' \
			'"{60}","{61}","{62}","{63}","{64}","{65}","{66}","{67}","{68}","{69}",' \
			'"{70}"'.format( \
			self.userProvince, self.userLevelName, self.price, self.userClientShow, \
			self.createTime, self.orderProcessSpeed, self.shipSpeed, self.deliverySpeed, \
			self.isOnTimeDelivery, self.isDeliveryCorrect, self.isDeliveryIntact, \
				self.isDifficultLastMile, self.isDeliveryLastMile, self.deliveryServiceAttitude, \
			self.installerArrivalTime, self.installerArrivalSpeed, self.installSpeed, \
				self.installResult, self.installerExplain, self.installerAttitude, \
			self.isInstallerArbitraryCharges, self.isBillComplete, self.isGiftPresentation, \
				self.isAfterSale, self.isReturnVisit, self.isGiftByAfterSale, \
			self.isConnectCustomerService, self.connectCustomerServiceReason, self.customerServiceEffectiveness, \
			self.isMaintain, self.maintainTimes, self.maintainResult, \
			self.isReplacement, self.replacementResult, self.replacementTimes, \
			self.isReturn, self.returnResult, self.retrunTimes, \
			self.afterSaleEffectiveness, self.afterSaleAttitude, self.isDemandResolved, \
			self.equipmentModel, \
			self.priceChanged, self.priceCompare, self.priceDifference, \
			self.functionalDiversity, self.energyEfficiency, self.performance, self.noiseFigure, \
				self.beautiful, self.complete, self.isBreakdown, self.failureIndex, self.EaseOfUse, \
			self.brandAwareness, self.productAwareness, \
			self.sftOfCostEffective, self.sftOfInsured, self.sftOfOrderProcess, self.sftOfDelivery, \
				self.sftOfInstallation, self.sftOfAfterSale, \
			self.sftOfProductQuality, self.sftOfProductConsistent, self.sftOfPrepurchaseExpectation, \
			self.score, self.sftLevel, self.compilation, \
			self.willOfRepurchasecategory, self.willOfRepurchaseBand, self.recommended)


if __name__ == '__main__':
	comment = Comment()
	print(comment)

