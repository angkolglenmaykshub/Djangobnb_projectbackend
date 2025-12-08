from django.http import JsonResponse


from rest_framework.decorators import api_view


from .models import Conversation, ConversationMessage
from .serializers import ConversationListSerializer, ConversationDetailSerializer


from useraccount.models import User




@api_view(['GET'])
def conversations_list(request):
    serializer = ConversationListSerializer(request.user.conversations.all(), many=True)


    return JsonResponse(serializer.data, safe=False)




@api_view(['GET'])
def conversations_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)


    conversation_serializer = ConversationDetailSerializer(conversation, many=False)
    # messages_serializer = ConversationMessageSerializer(conversation.messages.all(), many=True)


    return JsonResponse({
        'conversation': conversation_serializer.data,
        # 'messages': messages_serializer.data
    }, safe=False)




@api_view(['GET'])
def conversations_start(request, user_id):
    try:
        other_user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)


    conversation = Conversation.objects.filter(users=request.user).filter(users=other_user).first()


    if not conversation:
        conversation = Conversation.objects.create()
        conversation.users.add(request.user, other_user)


    serializer = ConversationDetailSerializer(conversation)
    return JsonResponse(serializer.data)