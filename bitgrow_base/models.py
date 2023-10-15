from django.db import models

# Create your models here.


# KOL
class KOL(models.Model):
    """
    Args:
        models (_type_): _description_
        name (str): 名称
        intro (str): 介绍
        avatar (url): 头像
        portrait (str): 画像
        quoted_price: 报价
        total_reward: 总回报金额

    """
    PORTRAIT_TYPE = [
        (1, "DAO"),
        (2, "DEFI"),
        (3, "NFT"),
        (4, "开发者")
    ]

    LANGUAGE_CHOICES = [
        (1, '英文'),
        (2, '韩文'),
        (3, '日文'),
        (4, '中文')
    ]

    AREA_TYPE = [
        (1, '美国'),
        (2, '韩国'),
        (3, '日本'),
        (4, '东南亚')
    ]

    name = models.CharField(max_length=28, null=True,
                            blank=True, verbose_name='名称')
    intro = models.CharField(max_length=100, null=True,
                             blank=True, verbose_name='介绍')

    avatar = models.URLField(
        max_length=300, null=True, blank=True, verbose_name="头像")

    connectable_user = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="可连接用户"
    )

    language = models.IntegerField(
        choices=LANGUAGE_CHOICES, null=True, blank=True, verbose_name="受众语言"
    )

    area = models.IntegerField(
        choices=AREA_TYPE,  blank=True, null=True, verbose_name="地区")

    average_display = models.IntegerField(
        null=True, blank=True, default=0, verbose_name="平均展示量"
    )

    portrait = models.IntegerField(
        choices=PORTRAIT_TYPE,
        null=True, blank=True, verbose_name="画像"
    )
    quoted_price = models.IntegerField(
        null=True, blank=True, verbose_name="报价")
    # 仅用于缓存
    total_reward = models.FloatField(
        null=True, blank=True, verbose_name="总回报"
    )
    claim_reward = models.FloatField(
        null=True, blank=True, verbose_name='可领取金额'
    )
    address = models.CharField(
        max_length=64, blank=True, null=True, verbose_name="区块链地址")

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = "KOL"
        verbose_name_plural = "KOL"


# Project
class Project(models.Model):
    """_s
    Args:
        name (str):项目名
        intro (str): 项目介绍
        avatar (url): 头像
        track (int): 赛道
        website (url): 官网
        twitter (str): 推特
        discord (str): discord
        contract (srf): 合约 
    """
    TRACK_TYPE = [
        (1, "DAO"),
        (2, "DEFI"),
        (3, "NFT"),
        (4, "Tool")
    ]
    name = models.CharField(max_length=28, null=True,
                            blank=True, verbose_name='项目名称')
    intro = models.CharField(max_length=200, null=True,
                             blank=True, verbose_name="项目介绍")
    avatar = models.URLField(max_length=200, null=True,
                             blank=True, verbose_name="头像")
    track = models.IntegerField(
        choices=TRACK_TYPE, null=True, blank=True, verbose_name="赛道")
    website = models.URLField(null=True, blank=True,
                              max_length=300, verbose_name="官网")
    twitter = models.CharField(
        max_length=64, blank=True, null=True, verbose_name="Twitter")
    discord = models.CharField(
        max_length=128, blank=True, null=True, verbose_name="Discord")
    contract = models.CharField(
        max_length=64, blank=True, null=True, verbose_name="智能合约")

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        verbose_name = '项目方'
        verbose_name_plural = '项目方'


# Task任务
class Task(models.Model):
    """
    Args:
        name(str): 任务名
        platform(int): 发布平台 (twitter/ telegram)
        area (int): 地区 (台湾/韩国/日本/新加坡)
        delivery_method: 派单方式 (派单/先到先到/招募)
        payment_method: 结算方式（直接结算/CPS结算/招募）
        task_type: 任务类型 (发布推文/撰写研报)
        fans_requirement: 接单条件 粉丝数限制
        requirement: 任务要求
        text: 推广文案
        price: 任务金额
        end_time: 截止时间
        people: 参与人数
        status: 任务状态
    """
    AREA_TYPE = [
        (1, '台湾'),
        (2, '韩国'),
        (3, '日本'),
        (4, '新加坡')
    ]

    PLATFORM_TYPE = [
        (1, 'twitter'),
        (2, 'telegram')
    ]

    DELIVERY_METHOD = [
        (1, '派单'),
        (2, '先到先得'),
        (3, '招募')
    ]

    PAYMENT_METHOD = [
        (1, '直接结算'),
        (2, 'CPS结算'),
        (3, '招募')
    ]

    TASK_TYPE = [
        (1, '发布推文'),
        (2, '撰写研报')
    ]

    STATUS = [
        (1, '进行中'),
        (2, '已结束')
    ]

    name = models.CharField(max_length=64, blank=True,
                            null=True, verbose_name="任务名")

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,  null=True, blank=True, verbose_name='项目')

    task_type = models.IntegerField(
        choices=TASK_TYPE, null=True, blank=True, verbose_name='任务类型'
    )

    platform = models.IntegerField(
        choices=PLATFORM_TYPE, blank=True, null=True, verbose_name="发布平台")
    area = models.IntegerField(
        choices=AREA_TYPE,  blank=True, null=True, verbose_name="地区")
    delivery_method = models.IntegerField(
        choices=DELIVERY_METHOD, blank=True, null=True, verbose_name='派单方式')
    payment_method = models.IntegerField(
        choices=DELIVERY_METHOD, blank=True, null=True, verbose_name='结算方式')
    fans_requirement = models.IntegerField(
        blank=True, null=True, verbose_name="粉丝数量限制")
    requirement = models.CharField(
        max_length=500,
        blank=True, null=True, verbose_name="任务要求"
    )

    price = models.FloatField(
        blank=True, null=True, verbose_name='任务金额'
    )

    text = models.CharField(
        max_length=500,
        blank=True, null=True, verbose_name="推广文案"
    )
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="结束时间")
    people = models.IntegerField(default=0, blank=True, verbose_name="参与人数")
    status = models.IntegerField(
        choices=STATUS, blank=True, default=1, verbose_name="任务状态")

    def __str__(self) -> str:
        if self.name:
            return self.name
        return 'No Name'

    class Meta:
        verbose_name = '任务'
        verbose_name_plural = '任务'


# Order
class Order(models.Model):
    """_summary_
    Args:
        order_id（str)：  订单ID 
        price (int): 价格
        status (int) : 订单状态
        kol (KOL): KOL  用于kol指派
        verify_url: 检验URL
    """
    STATUS_TYPE = [
        (1, '未接单'),
        (2, '进行中'),
        (3, '已完成'),
        (4, '待核验'),
        (5, '已取消')
    ]

    order_id = models.CharField(
        max_length=32, null=True, blank=True, verbose_name='订单ID')

    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, null=True, blank=True, verbose_name='任务')

    kol = models.ForeignKey(KOL, on_delete=models.CASCADE,
                            null=True, blank=True, verbose_name='KOL')

    price = models.FloatField(
        null=True, blank=True, verbose_name='订单金额'
    )

    status = models.IntegerField(
        choices=STATUS_TYPE,
        null=True, blank=True, verbose_name='订单状态'
    )

    verify_url = models.URLField(
        max_length=200, null=True, blank=True, verbose_name='核验URL'
    )

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'

    def __str__(self) -> str:
        if self.order_id:
            return str(self.order_id)
        return str('No Id')
