"""

Time: :2023/10/13 12:50:40

"""


from django.shortcuts import render
from . import models, serializers

from rest_framework import mixins, status, viewsets
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response
from django.http import JsonResponse


from . import filters

# Create your views here.


class KOLViewSet(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    """
    KOL ViewSet
    """
    serializer_class = serializers.KOLSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    # 指定过滤器
    filterset_class = filters.KOLFilter

    def get_queryset(self):
        return models.KOL.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    Project ViewSet
    """

    serializer_class = serializers.ProjectSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return models.Project.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        pass


class OrderViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = serializers.OrderSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    # 指定过滤器
    filterset_class = filters.OrderFilter

    def get_queryset(self):
        return models.Order.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        1.project: choose KOL to create order with creating task
        data
        projectId 项目id
        platform 发送平台 1推特 2TG
        area 1->美国 2->韩国 3-> 日本 4-> 新加坡
        taskName 任务名
        deliveryMethod 派单方式
        paymentMethod 结算方式 
        taskType 任务
        fansRequirement 粉丝数量要求
        text 文案 
        price 订单价格
        endTime 结束时间
        orderId 订单ID
        kol KOL ID
        2.KOL: choose task to create order 
        create order by taskId


        """

        """ 
        1.
        Returns:
            _type_: _description_
        """

        task_id = request.POST.get('taskId', None)
        order_id = request.POST.get('orderId', None)
        kol = request.POST.get('kol', None)
        print(task_id)
        if task_id:
            try:
                task = models.Task.objects.get(id=task_id)
                models.Order.objects.create(
                    order_id=order_id,
                    task=task,
                    kol_id=kol,
                    price=task.price,
                    status=2,  # 已接单
                )
                return Response({'Create Success'})
            except:
                return Response({'Task Not Found'})
        else:
            project = request.POST.get('project', None)
            area = request.POST.get('area', None)
            delivery_method = request.POST.get('deliveryMethod', None)
            payment_method = request.POST.get('paymentMethod', None)
            task_type = request.POST.get('taskType', None)
            task_name = request.POST.get('taskName', None)
            fans_requirement = request.POST.get('taskType', None)
            text = request.POST.get('text', None)
            end_time = request.POST.get('end_time', None)

            print('task_name', task_name)
            price = request.POST.get('price', None)

            new_task = models.Task.objects.create(
                project=project,
                area=area,
                delivery_method=delivery_method,
                payment_method=payment_method,
                task_type=task_type,
                fans_requirement=fans_requirement,
                text=text,
                price=price,
                end_time=end_time,
                name=task_name
            )

            models.Order.objects.create(
                order_id=order_id,
                task=new_task,
                kol_id=kol,
                price=price,
                status=1,  # 未接单
            )
            return Response({'success'})

    def update(self, request, *args, **kwargs):
        """
        更改订单：
        1.项目方完成验证 不做
        2.KOL接受派单 

        3.KOL提交审核

        """
        action = request.data.get('action')
        order = self.get_object()

        if action == 'acceptOrder':
            order.status = 2
            order.save()
        # order = models.Order.objects.get()
            return Response({'code': 1, 'msg': 'update success'}, status=status.HTTP_200_OK)
        if action == 'submitVerify':
            verify_url = request.data.get('verifyUrl')
            order.status = 4
            order.verify_url = verify_url
            order.save()
        return Response({'code': 0, 'msg': 'update success'}, status=status.HTTP_204_NO_CONTENT)


class TaskViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = serializers.TaskSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.TaskFilter

    def get_queryset(self):
        return models.Task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # todo创建任务
        project = request.POST.get('project', None)
        area = request.POST.get('area', None)
        delivery_method = request.POST.get('deliveryMethod', None)
        payment_method = request.POST.get('paymentMethod', None)
        task_type = request.POST.get('taskType', None)
        task_name = request.POST.get('taskName', None)
        fans_requirement = request.POST.get('taskType', None)
        text = request.POST.get('text', None)
        end_time = request.POST.get('end_time', None)

        price = request.POST.get('price', None)

        models.Task.objects.create(
            project=project,
            area=area,
            delivery_method=delivery_method,
            payment_method=payment_method,
            task_type=task_type,
            fans_requirement=fans_requirement,
            text=text,
            price=price,
            end_time=end_time,
            name=task_name
        )

        return Response({'create task success'})
