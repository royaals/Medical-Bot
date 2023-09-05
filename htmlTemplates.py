css = """
<style>
.chat-message {
    padding: 4.5rem; border-radius: 5.5rem; margin-bottom: 2rem; display: flex
}
.chat-message.user {
    background-color: #43411b;
}
.chat-message.bot {
    background-color: #A1CCD1;
}
.chat-message .avatar {
  width: 50%;
  height:50px;
}
.chat-message .avatar img {
  max-width: 60px;
  max-height: 50px;
  border-radius:50%;
  
}
.chat-message .message {
    width: 70%;
    padding: -117.5rem;
    color: #fff;
}
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <img src="" style="max-height: 178px; max-width: 278px; border-radius: 150%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""

user_template = """
<div class="chat-message user">
    <div class="avatar">
        <img src="">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
"""
