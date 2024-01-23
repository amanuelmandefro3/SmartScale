import json
from channels.generic.websocket import AsyncWebsocketConsumer
from firebase_admin import db

class FirebaseUpdatesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Connect to Firebase and listen for changes
        ref = db.reference('/your_firebase_path')
        ref.listen(self.firebase_callback)

    async def firebase_callback(self, event):
        # Send the Firebase data update to the WebSocket
        await self.send(text_data=json.dumps({'message': event.data}))
