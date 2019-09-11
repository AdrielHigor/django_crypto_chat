from django.views.generic import TemplateView  # , CreateView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse
# from django.http import JsonResponse
# from django.template.loader import render_to_string
# import json
# from app.core.models import User
# from app.chat.models import Chat, Message
# from asgiref.sync import async_to_sync


@method_decorator(login_required(login_url='/user/login'), name='dispatch')
class HomeView(TemplateView):
    template_name = "chat/chat.html"

# class ChatView(LoginRequiredMixin, TemplateView):
#     template_name = 'chat/chat.html'

#     def get_context_data(self, **kwargs):
#         context = super(ChatView, self).get_context_data()

#         if Chat.objects.count():
#             context['messages'] = Chat.objects.first().messages.all()
#         else:
#             room = Chat.objects.create()
#             room.users.add(self.request.user)

#         return context


# class MessageCreateView(LoginRequiredMixin, CreateView):
#     model = Message
#     fields = ['text', 'chat', 'sender']

#     def post(self, request, *args, **kwargs):
#         message = request.POST.get('message', None)
#         sender = int(request.POST.get('sender', None))
#         if message and sender:
#             new_message = Message.objects.create(
#                 chat=Chat.objects.first(),
#                 sender=User.objects.get(pk=sender),
#                 text=message
#             )
#             args = {'message': new_message}
#             recipient_message = render_to_string(
#                 'partials/other-message-html.html', args)
#             sender_message = render_to_string(
#                 'partials/my-message-html.html', args)

#             async_to_sync(channel_layer.group_send)("chat", {"type": "chat.force_disconnect"})

#             Group("room").send({
#                 "text": json.dumps({
#                     "recipient_message": recipient_message,
#                     "sender_message": sender_message,
#                     "sender": self.request.user.pk
#                 })
#             })

#             return JsonResponse(
#                 dict(recipient_message=recipient_message,
#                      sender_message=sender_message)
#             )
#         return HttpResponse('')


# class MessageTypingView(View):
#     def post(self, request, *args, **kwargs):
#         user_pk = self.request.POST.get('user', 0)
#         user = User.objects.get(pk=user_pk)
#         Group("room").send({
#             "text": json.dumps({
#                 'action': 'typing',
#                 'user': user_pk,
#                 'username': user.username
#             }),
#         })

#         return HttpResponse("Hello, test")
