# chatgpt-plugin

# work in progress

## The goal of this repo is to build a chatgpt-plugin implemented in Nuvolars that processes Figma Files generating an user interface. 

We espect to send to ChatGpt API this JSON obtained from FIGMA:

```{'document': {'id': '0:0', 'name': 'Document', 'type': 'DOCUMENT', 'scrollBehavior': 'SCROLLS', 'children': [{'id': '0:1', 'name': 'Page 1', 'type': 'CANVAS', 'scrollBehavior': 'SCROLLS', 'children': [{'id': '9:3', 'name': 'HELLO CHATGPT!', 'type': 'TEXT', 'scrollBehavior': 'SCROLLS', 'blendMode': 'PASS_THROUGH', 'absoluteBoundingBox': {'x': -236.0, 'y': -356.0, 'width': 263.0, 'height': 59.0}, 'absoluteRenderBounds': {'x': -227.8515625, 'y': -341.79998779296875, 'width': 247.6514129638672, 'height': 24.8699951171875}, 'constraints': {'vertical': 'TOP', 'horizontal': 'LEFT'}, 'fills': [{'blendMode': 'NORMAL', 'type': 'SOLID', 'color': {'r': 0.0, 'g': 0.0, 'b': 0.0, 'a': 1.0}}], 'strokes': [], 'strokeWeight': 1.0, 'strokeAlign': 'OUTSIDE', 'effects': [], 'characters': 'HELLO CHATGPT!', 'style': {'fontFamily': 'Indie Flower', 'fontPostScriptName': 'IndieFlower-Regular', 'fontWeight': 400, 'fontSize': 30.0, 'textAlignHorizontal': 'CENTER', 'textAlignVertical': 'CENTER', 'letterSpacing': 3.0, 'lineHeightPx': 43.77000045776367, 'lineHeightPercent': 100.0, 'lineHeightUnit': 'INTRINSIC_%'}, 'layoutVersion': 4, 'characterStyleOverrides': [], 'styleOverrideTable': {}, 'lineTypes': ['NONE'], 'lineIndentations': [0]}, {'id': '9:5', 'name': 'If you are reading these words, it’s cause the ChatGpt API is rendering a Figma file automatically in html', 'type': 'TEXT', 'scrollBehavior': 'SCROLLS', 'blendMode': 'PASS_THROUGH', 'absoluteBoundingBox': {'x': -720.0, 'y': -248.0, 'width': 1271.0, 'height': 22.0}, 'absoluteRenderBounds': {'x': -481.5400390625, 'y': -244.39999389648438, 'width': 794.24560546875, 'height': 18.720001220703125}, 'constraints': {'vertical': 'TOP', 'horizontal': 'LEFT'}, 'fills': [{'blendMode': 'NORMAL', 'type': 'SOLID', 'color': {'r': 0.0, 'g': 0.0, 'b': 0.0, 'a': 1.0}}], 'strokes': [], 'strokeWeight': 1.0, 'strokeAlign': 'OUTSIDE', 'effects': [], 'characters': 'If you are reading these words, it’s cause the ChatGpt API is rendering a Figma file automatically in html', 'style': {'fontFamily': 'Indie Flower', 'fontPostScriptName': 'IndieFlower-Regular', 'fontWeight': 400, 'textAutoResize': 'HEIGHT', 'fontSize': 15.0, 'textAlignHorizontal': 'CENTER', 'textAlignVertical': 'CENTER', 'letterSpacing': 1.5, 'lineHeightPx': 21.885000228881836, 'lineHeightPercent': 100.0, 'lineHeightUnit': 'INTRINSIC_%'}, 'layoutVersion': 4, 'characterStyleOverrides': [], 'styleOverrideTable': {}, 'lineTypes': ['NONE'], 'lineIndentations': [0]}], 'backgroundColor': {'r': 0.987500011920929, 'g': 0.9586979150772095, 'b': 0.9586979150772095, 'a': 1.0}, 'prototypeStartNodeID': None, 'flowStartingPoints': [], 'prototypeDevice': {'type': 'NONE', 'rotation': 'NONE'}, 'exportSettings': [{'suffix': '', 'format': 'PNG', 'constraint': {'type': 'SCALE', 'value': 1.0}}]}]}, 'components': {}, 'componentSets': {}, 'schemaVersion': 0, 'styles': {}, 'name': 'Untitled', 'lastModified': '2023-09-08T11:00:15Z', 'thumbnailUrl': 'https://s3-alpha.figma.com/thumbnails/0a9c06c1-f12b-4330-93a7-e2fd779f0f2b?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAQ4GOSFWC3B66D3S5%2F20230907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230907T000000Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=735205ebd28f5b5cd3383179d87bd319b689c50c1363b4addfccc0d7c7dfae13', 'version': '4128584905', 'role': 'owner', 'editorType': 'figma', 'linkAccess': 'view'} ```

And then to obtain
```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ChatGPT Plugin</title>
  <style>
    body {
      background-color: #FBE6E6;
      margin: 0;
      padding: 0;
      font-family: 'Indie Flower', cursive;
    }

    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    .title {
      font-size: 30px;
      font-weight: 400;
      text-align: center;
      letter-spacing: 3px;
      line-height: 44px;
      color: #000;
    }

    .description {
      font-size: 15px;
      font-weight: 400;
      text-align: center;
      letter-spacing: 1.5px;
      line-height: 22px;
      color: #000;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1 class="title">HELLO CHATGPT!</h1>
    <p class="description">If you are reading these words, it’s cause the ChatGpt API is rendering a Figma file automatically in html</p>
  </div>
</body>
</html>
```
For this reason, we are implementing scripts. Some of these will call the Figma APIs, while others will call the chatGpt APIs, passing the responses from Figma and requesting the HTML and CSS in return.
