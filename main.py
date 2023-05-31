
from flask import Flask, render_template, request, jsonify, make_response
app = Flask(__name__)


@app.route("/")
def helloworld():
    return render_template('base.html')


@app.route("/chat_video", methods=['GET'])
def chat_video():
    return render_template('chat_video.html')

@app.route("/summarize", methods=['POST'])
def summarize():
    request_params = request.get_json()
    video_url = request_params['video_url']
    video_id = request_params['video_id']
    # Here implement the logic to summarize the video
    summary = "Here is the long text summarizing the video"
    data = {'summary': summary}
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/video_summary", methods=['GET'])
def video_summary():
    return render_template('video_summary.html')

@app.route("/video_chat", methods=['POST'])
def video_chat():
    request_params = request.get_json()
    message = request_params['message']
    data = {'answer': message, 'sources': 'https://youtu.be/tPJqAk1GA-A?start=40, https://youtu.be/tPJqAk1GA-A?t=30'}
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route("/process_video", methods=['post'])
def process_video():
    import time
    time.sleep(5)
    request_params = request.get_json()
    video_url = request_params['video_url']
    video_id = video_url.split('v=')[-1]
    data = {'video_url': 'https://youtu.be/{}'.format(video_id)}
    response = make_response(jsonify(data))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response



if __name__ == "__main__":
    app.run()