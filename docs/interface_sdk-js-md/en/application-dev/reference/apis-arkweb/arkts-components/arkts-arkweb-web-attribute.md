# Web properties/events

Defines the Web attribute functions.

**Inheritance/Implementation:** WebAttribute extends CommonMethod<WebAttribute>

**Since:** 8

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## aiSessionOptions

```TypeScript
aiSessionOptions(aiSessions: Array<AISessionEvent>)
```

Configures custom frontend AI sessions for the **Web** component, used to register multiple custom AI sessions.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aiSessions | Array&lt;[AISessionEvent](arkts-arkweb-aisessionevent-i.md)&gt; | Yes | Array of frontend AI session configuration objects. Each object contains an AI session type and the corresponding lifecycle callback methods. Currently, only models included in [AISessionType](arkts-arkweb-aisessiontype-e.md) are supported. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct DemoPage {
  private webController: webview.WebviewController = new webview.WebviewController();
  sessions: Map<string, string> = new Map<string, string>();

  onCreateAISession = (id: string, params: string, result: OnAISessionCallback): boolean => {
    this.sessions.set(id, params); // Simulate creating an AI session.
    console.info(`[AISession]onCreateAISession params: ${params}`);
    // Notify the caller that the AI session is created successfully.
    result(AISessionResultType.SUCCESS, "AISession created");
    return true;
  }

  onExecuteAIAction = (id: string, params: string, result: OnAISessionCallback): void => {
    this.sessions.get(id); // Simulate retrieving the session and executing an action.
    console.info(`[AISession]onExecuteAIAction params: ${params}`);
    // Simulate streaming the AI execution result: multiple RUNNING calls indicate the task is in progress and return data chunks, and a final SUCCESS call indicates task completion.
    result(AISessionResultType.RUNNING, "AISession chunk 1\n");
    result(AISessionResultType.RUNNING, "AISession chunk 2\n");
    result(AISessionResultType.SUCCESS, "AISession chunk end\n");
  }

  onDestroyAISession = (id: string): void => {
    this.sessions.delete(id); // Simulate destroying the session and releasing resources.
  }

  @State options: AISessionEvent = {
    aiSessionType: AISessionType.SUMMARIZER,
    onCreateAISession: this.onCreateAISession,
    onExecuteAIAction: this.onExecuteAIAction,
    onDestroyAISession: this.onDestroyAISession
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.webController })
        .aiSessionOptions([this.options])
    }
    .width('100%')
    .height('100%')
  }
}
```

HTML file to be loaded

```TypeScript
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>Summarizer API Test</title>
</head>
<body style="max-width:600px;margin:20px auto;padding:0 16px;">
  <p id="status">checking...</p>
  <button id="initBtn" onclick="init()">Create Session</button>
  <br><br>
  <textarea id="input" rows="6" style="width:100%;font:inherit" placeholder="paste text to summarize"></textarea>
  <br><br>
  <button id="btn" onclick="run()" disabled>Summarize</button>
  <pre id="result"></pre>
  <script>
    let s;
    (async () => {
      const d = document.getElementById('status');
      if (!('Summarizer' in self)) { d.textContent = 'API not supported'; return; }
      const a = await Summarizer.availability();
      d.textContent = 'Summarizer: ' + a;
      if (a === 'unavailable') document.getElementById('initBtn').disabled = true;
    })();

    async function init() {
      const d = document.getElementById('status'), ib = document.getElementById('initBtn');
      ib.disabled = true;
      d.textContent = 'creating...';
      try {
        s = await Summarizer.create({
          type: 'tldr', length: 'medium', format: 'plain-text',
          monitor(m) { m.addEventListener('downloadprogress', e => { d.textContent = 'downloading ' + (e.loaded * 100 | 0) + '%' }); }
        });
        d.textContent = 'ready';
        document.getElementById('btn').disabled = false;
      } catch (e) { d.textContent = 'Error: ' + e.message; ib.disabled = false; }
    }

    async function run() {
      const t = document.getElementById('input').value.trim();
      if (!t || !s) return;
      const btn = document.getElementById('btn'), r = document.getElementById('result');
      btn.disabled = true;
      r.textContent = '...';
      try { r.textContent = await s.summarize(t); }
      catch (e) { r.textContent = 'Error: ' + e.message; }
      btn.disabled = false;
    }
  </script>
</body>
</html>
```

## allowWindowOpenMethod

```TypeScript
allowWindowOpenMethod(flag : boolean)
```

Sets whether to allow a new window to automatically open through JavaScript.

> **NOTE：**
> 
> - This API takes effect only when [javaScriptAccess](#javascriptaccess) is enabled.
> 
> - This API opens a new window when [multiWindowAccess](#multiwindowaccess) is enabled, and a
> local window when it is disabled.
> 
> - The default value of **flag** is subject to the settings of the **persist.web.allowWindowOpenMethod.enabled**
> system attribute. If this attribute is not set, the default value of **flag** is **false**.
> 
> - Run the **hdc shell param get persist.web.allowWindowOpenMethod.enabled** command to check whether the system
> attribute **persist.web.allowWindowOpenMethod.enabled** is enabled. If the attribute value is **1**, the system
> attribute is enabled. If the attribute value is **0** or does not exist, the system attribute is disabled. You
> can run the **hdc shell param set persist.web.allowWindowOpenMethod.enabled 1** command to enable the system
> attribute.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| flag | boolean | Yes | Whether to allow a new window to automatically open through JavaScript. The value **true** means to allow a new window to automatically open through JavaScript, and **false** means only to allow a new window to automatically open through JavaScript using user behaviors. The user behavior here refers to a user requests to open a new window (**window.open**) within 5 seconds after operating the **Web** component. The default value of **flag** is subject to the settings of the **persist.web.allowWindowOpenMethod.enabled** system attribute. If this attribute is set to **true**, the default value of **flag** is **true**. If this attribute is not set, the default value of **flag** is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

// There are two Web components on the same page. When the WebComponent object opens a new window, the NewWebViewComp object is displayed.
@CustomDialog
struct NewWebViewComp {
    controller?: CustomDialogController;
    webviewController1: webview.WebviewController = new webview.WebviewController();

    build() {
        Column() {
            Web({ src: "", controller: this.webviewController1 })
                .javaScriptAccess(true)
                .multiWindowAccess(false)
                .onWindowExit(() => {
                    console.info("NewWebViewComp onWindowExit");
                    if (this.controller) {
                        this.controller.close();
                    }
                })
                .onActivateContent(() => {
                    // The Web component needs to be displayed in the foreground. The app is advised to perform tab or window switching here.
                    console.info("NewWebViewComp onActivateContent")
                })
        }
    }
}

@Entry
@Component
struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();
    dialogController: CustomDialogController | null = null;

    build() {
        Column() {
            Web({ src: $rawfile("index.html"), controller: this.controller })
                .javaScriptAccess(true)
                // MultiWindowAccess needs to be enabled.
                .multiWindowAccess(true)
                .allowWindowOpenMethod(true)
                .onWindowNew((event) => {
                    if (this.dialogController) {
                        this.dialogController.close()
                    }
                    let popController: webview.WebviewController = new webview.WebviewController();
                    this.dialogController = new CustomDialogController({
                        builder: NewWebViewComp({ webviewController1: popController }),
                        // Set isModal to false to prevent the new window from being destroyed, so that the onActivateContent callback can be triggered.
                        isModal: false
                    })
                    this.dialogController.open();
                    // Return the WebviewController object corresponding to the new window to the web kernel.
                    // If event.handler.setWebController is not called, the rendering process will be blocked.
                    // If no new window is created, set the value of event.handler.setWebController to null to notify the Web component that no new window is created.
                    event.handler.setWebController(popController);
                })
        }
    }
}
```

Example of the HTML file

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<div>
    <button type="button" onclick="delayOpenwindow(5000)">delayOpenwindow_5s</button>
</div>

<script>
    function openwindowAll(){
        open("https://www.example.com","_blank","height=400,width=600,top=100,left=100,scrollbars=no")
    }
    function delayOpenwindow(t){
        setTimeout(openwindowAll, t);
    }
</script>
</body>
</html>
```

## backToTop

```TypeScript
backToTop(backToTop: boolean)
```

Sets whether to enable the back-to-top feature for the **Web** component when the status bar is touched. When this attribute is not explicitly called, the back-to-top feature for the status bar is enabled by default.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| backToTop | boolean | Yes | Whether to enable the back-to-top feature. The value **true** means to enable the feature, and **false** means the opposite. When **undefined** or **null** is passed in, the value is **true**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .backToTop(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
         font-size:16px;
         height:200px;
         text-align: center;       /* Horizontally centered */
         line-height: 200px;       /* Vertically centered (the height matches the container height) */
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>
```

## bindSelectionMenu

```TypeScript
bindSelectionMenu(elementType: WebElementType, content: CustomBuilder, responseType: WebResponseType,
      options?: SelectionMenuOptionsExt)
```

Sets the custom selection menu.

**Since:** 13

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementType | [WebElementType](arkts-arkweb-webelementtype-e.md) | Yes | Menu type. |
| content | [CustomBuilder](../../apis-arkui/arkts-components/arkts-arkui-custombuilder-t.md) | Yes | Menu content. |
| responseType | [WebResponseType](arkts-arkweb-webresponsetype-e.md) | Yes | Response type of the menu. |
| options | [SelectionMenuOptionsExt](arkts-arkweb-selectionmenuoptionsext-i.md) | No | Menu options. The default configuration is used when undefined or null is passed in. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { pasteboard } from '@kit.BasicServicesKit';
import { BusinessError } from '@kit.BasicServicesKit';

interface PreviewBuilderParam {
  width: number;
  height: number;
  url:Resource | string | undefined;
}

interface PreviewBuilderParamForImage {
  previewImage: Resource | string | undefined;
  width: number;
  height: number;
}


@Builder function PreviewBuilderGlobalForImage($$: PreviewBuilderParamForImage) {
  Column() {
    Image($$.previewImage)
      .objectFit(ImageFit.Fill)
      .autoResize(true)
  }.width($$.width).height($$.height)
}

@Entry
@Component
struct SelectionMenuLongPress {
  controller: webview.WebviewController = new webview.WebviewController();
  previewController: webview.WebviewController = new webview.WebviewController();
  @Builder PreviewBuilder($$: PreviewBuilderParam){
    Column() {
      Stack(){
        Text("") // Select whether to display the URL.
          .padding(5)
          .width('100%')
          .textAlign(TextAlign.Start)
          .backgroundColor(Color.White)
          .copyOption(CopyOptions.LocalDevice)
          .maxLines(1)
          .textOverflow({overflow:TextOverflow.Ellipsis})
        Progress({ value: this.progressValue, total: 100, type: ProgressType.Linear }) // Display the progress bar.
          .style({ strokeWidth: 3, enableSmoothEffect: true })
          .backgroundColor(Color.White)
          .opacity(this.progressVisible?1:0)
          .backgroundColor(Color.White)
      }.alignContent(Alignment.Bottom)
      Web({src:$$.url,controller: new webview.WebviewController()})
        .javaScriptAccess(true)
        .fileAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .domStorageAccess(true)
        .onPageBegin(()=>{
          this.progressValue = 0;
          this.progressVisible = true;
        })
        .onProgressChange((event)=>{
          this.progressValue = event.newProgress;
        })
        .onPageEnd(()=>{
          this.progressVisible = false;
        })
        .hitTestBehavior(HitTestMode.None) // Disable the gesture response during web page preview.
    }.width($$.width).height($$.height) // Set the preview width and height.
  }

  private result: WebContextMenuResult | undefined = undefined;
  @State previewImage: Resource | string | undefined = undefined;
  @State previewWidth: number = 1;
  @State previewHeight: number = 1;
  @State previewWidthImage: number = 1;
  @State previewHeightImage: number = 1;
  @State linkURL:string = "";
  @State progressValue:number = 0;
  @State progressVisible:boolean = true;
  uiContext: UIContext = this.getUIContext();
  enablePaste = false;

  clearSelection() {
    try {
      this.controller.runJavaScript(
        'clearSelection()',
        (error, result) => {
          if (error) {
            console.error(`run clearSelection JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
            return;
          }
          if (result) {
            console.info(`The clearSelection() return value is: ${result}`);
          }
        });
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
    }
  }


  @Builder
  LinkMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy Link', })
        .onClick(() => {
          const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, this.linkURL);
          const systemPasteboard = pasteboard.getSystemPasteboard();
          systemPasteboard.setData(pasteboardData);
        })
      MenuItem({content:'Open Link'})
        .onClick(()=>{
          this.controller.loadUrl(this.linkURL);
        })
    }
  }
  @Builder
  ImageMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy Image', })
        .onClick(() => {
          this.result?.copyImage();
          this.result?.closeContextMenu();
        })
    }
  }
  @Builder
  TextMenuBuilder() {
    Menu() {
      MenuItem({ content: 'Copy', })
        .onClick(() => {
          try {
            this.controller.runJavaScript(
              'copySelectedText()',
              (error, result) => {
                if (error) {
                  console.error(`run copySelectedText JavaScript error, ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
                  return;
                }
                if (result) {
                  console.info(`The copySelectedText() return value is: ${result}`);
                }
              });
          } catch (error) {
            console.error(`Failed to clear selection. Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
          }
          this.clearSelection()
        }).backgroundColor(Color.Pink)
    }
  }
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .javaScriptAccess(true)
        .fileAccess(true)
        .onlineImageAccess(true)
        .imageAccess(true)
        .domStorageAccess(true)
        .bindSelectionMenu(WebElementType.TEXT, this.TextMenuBuilder, WebResponseType.LONG_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {},
            menuType: MenuType.SELECTION_MENU,
          })
        .bindSelectionMenu(WebElementType.LINK, this.LinkMenuBuilder, WebResponseType.LONG_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {
              this.result?.closeContextMenu();
            },
            preview: this.PreviewBuilder({
              width: 500,
              height: 400,
              url:this.linkURL
            }),
            menuType: MenuType.PREVIEW_MENU
          })
        .bindSelectionMenu(WebElementType.IMAGE, this.ImageMenuBuilder, WebResponseType.LONG_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {
              this.result?.closeContextMenu();
            },
            preview: PreviewBuilderGlobalForImage({
              previewImage: this.previewImage,
              width: this.previewWidthImage,
              height: this.previewHeightImage,
            }),
            menuType: MenuType.PREVIEW_MENU,
          })
        .zoomAccess(true)
        .onContextMenuShow((event) => {
          if (event) {
            this.result = event.result;
            this.previewWidthImage = this.uiContext!.px2vp(event.param.getPreviewWidth());
            this.previewHeightImage = this.uiContext!.px2vp(event.param.getPreviewHeight());
            if (event.param.getSourceUrl().indexOf("resource://rawfile/") == 0) {
              this.previewImage = $rawfile(event.param.getSourceUrl().substring(19));
            } else {
              this.previewImage = event.param.getSourceUrl();
            }
            this.linkURL = event.param.getLinkUrl()
            // The value **true** indicates that the system default context menu is intercepted and a custom menu is used.
            return true;
          }
          return false;
        })
    }

  }
  // Swipe back
  onBackPress(): boolean | void {
    if (this.controller.accessStep(-1)) {
      this.controller.backward();
      return true;
    } else {
      return false;
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Touch and hold to copy text</title>
    <style>
        .container {
            background-color: white;
            padding: 30px;
            margin: 20px 0;
        }

        .context {
            line-height: 1.8;
            font-size: 18px;
        }

        .context span {
            border-radius: 8px;
            background-color: #f8f9fa;
        }

        .context a {
            color: #3498db;
            text-decoration: none;
            font-size: 18px;
            font-weight: 600;
            padding: 12px 24px;
            border: 2px solid #3498db;
            border-radius: 30px;
            display: inline-block;
            position: relative;
            overflow: hidden;
            margin-bottom: 20px;
        }

        .context img {
            max-width: 100%;
            height: auto;
            display: block;
            margin-bottom: 20px;
        }

        .context:hover img {
            transform: scale(1.05);
        }
    </style>
</head>
<body>
<div class="container">

    <div class="context">
        <!--img.png is in the same directory as the html file-->
        <img src="img.png">
    </div>

    <div class="context">
        <a  href="https://www.example.com">Touch and hold the link to display the menu</a>
    </div>

    <div class="context">
        <span>In this digital age, the text copying functionality has grown increasingly important. Whether quoting famous remarks, saving key information, or sharing interesting content, copying text is an integral part of our daily operations.</span>
    </div>

</div>
<br>

<script>
    function copySelectedText() {
        const selectedText = window.getSelection().toString();
        if (selectedText.length > 0) {
            // Use the Clipboard API to copy text.
            navigator.clipboard.writeText(selectedText)
                .then(() => {
                    showNotification();
                })
                .catch(err => {
                    console.error('Copy failed:', err);
                });
        }
    }
     function clearSelection() {
        if (window.getSelection) {
            window.getSelection().removeAllRanges();
        }
    }
</script>
</body>
</html>
```

## blankScreenDetectionConfig

```TypeScript
blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig)
```

Sets the blank screen detection configuration, such as whether to enable the detection, detection time, and detection policy. When this attribute is not explicitly called, blank screen detection is disabled by default.

> **NOTE：**
> 
> - Based on the configuration of **detectConfig**,
> [onDetectedBlankScreen](#ondetectedblankscreen) may be triggered when a blank screen or near-
> blank screen is detected after a web page is loaded.
> 
> - The setting takes effect in the next navigation.
> 
> - After the user interacts with the web page, the system does not check whether a blank screen occurs.
> 
> - This feature is not supported when **layoutMode** is set to **WebLayoutMode.FIT_CONTENT**.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| detectConfig | [BlankScreenDetectionConfig](arkts-arkweb-blankscreendetectionconfig-i.md) | Yes | Blank screen detection policy. |

**Examples**

```TypeScript
// blankScreenDetectionConfig.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .blankScreenDetectionConfig({
          enable: true,
          detectionTiming: [2, 4, 6, 8],
          contentfulNodesCountThreshold: 4,
          detectionMethods:[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN]
        })
        .onDetectedBlankScreen((event: BlankScreenDetectionEventInfo)=>{
          console.info(`Found blank screen on ${event.url}.`);
          console.info(`The blank screen reason is ${event.blankScreenReason}.`);
          console.info(`The blank screen detail is ${event.blankScreenDetails?.detectedContentfulNodesCount}.`);
        })
    }
  }
}
```

## blockNetwork

```TypeScript
blockNetwork(block: boolean)
```

Sets whether to block online downloads. When this attribute is not explicitly called, online resources can be loaded by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| block | boolean | Yes | Whether to allow online downloads. The value **true** means to block online downloads, and **false** means the opposite. If **undefined** or **null** is passed in, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State block: boolean = true;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .blockNetwork(this.block)
    }
  }
}
```

## blurOnKeyboardHideMode

```TypeScript
blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode)
```

Sets the blur mode for **Web** elements when the soft keyboard is dismissed. If this attribute is not explicitly called, the [BlurOnKeyboardHideMode.SILENT](arkts-arkweb-bluronkeyboardhidemode-e.md) mode is used by default.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [BlurOnKeyboardHideMode](arkts-arkweb-bluronkeyboardhidemode-e.md) | Yes | Whether to enable blur mode of the web element when soft keyboard is hidden. The default value is **BlurOnKeyboardHideMode.SILENT**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State blurMode: BlurOnKeyboardHideMode = BlurOnKeyboardHideMode.BLUR;
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .blurOnKeyboardHideMode(this.blurMode)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>blurOnKeyboardHideMode Demo</h1>
    <input type="text" id="input_a">
    <script>
      const inputElement = document.getElementById('input_a');
      inputElement.addEventListener('blur', function() {
        console.info('Input has lost focus');
      });
    </script>
  </body>
</html>
```

## bypassVsyncCondition

```TypeScript
bypassVsyncCondition(condition: WebBypassVsyncCondition)
```

Sets the rendering process to bypass vsync (vertical synchronization) scheduling and directly trigger drawing when the **scrollBy** API is called to scroll the page. When this attribute is not explicitly called, vsync scheduling is not skipped by default.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | [WebBypassVsyncCondition](arkts-arkweb-webbypassvsynccondition-e.md) | Yes | Condition for triggering the rendering process to bypass vsync scheduling. When **undefined** or **null** is passed in, the value is **NONE**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  condition: WebBypassVsyncCondition = WebBypassVsyncCondition.SCROLLBY_FROM_ZERO_OFFSET;

  build() {
    Column() {
      Button('scrollBy')
        .onClick(() => {
          this.controller.scrollBy(0, 5);
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .bypassVsyncCondition(this.condition)
    }
  }
}
```

## cacheMode

```TypeScript
cacheMode(cacheMode: CacheMode)
```

Sets the cache mode. When this attribute is not explicitly called, the default value **CacheMode.Default** is used.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cacheMode | [CacheMode](arkts-arkweb-cachemode-e.md) | Yes | Cache mode to set. When **undefined** or **null** is passed in, the value is **CacheMode.Default**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: CacheMode = CacheMode.None;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .cacheMode(this.mode)
    }
  }
}
```

## copyOptions

```TypeScript
copyOptions(value: CopyOptions)
```

Sets the clipboard copy scope option. If this attribute is not explicitly called, pasting across all apps on the current device is supported by default after copying.

> **NOTE：**
> 
> When this attribute is set to **CopyOptions.None**, the **enablePreviewMenu** configuration item in
> [dataDetectorConfig](#datadetectorconfig) does not take effect. When
> [enableDataDetector](#enabledatadetector) is set to **true** and this attribute is set to
> **CopyOptions.LocalDevice**, the AI menu feature is activated.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | CopyOptions | Yes | Pasteboard copy options. When **undefined** or **null** is passed in, the value is **CopyOptions.None**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .copyOptions(CopyOptions.None)
    }
  }
}
```

## darkMode

```TypeScript
darkMode(mode: WebDarkMode)
```

Sets the dark mode of the **Web** component. If this attribute is not explicitly called, dark mode is disabled by default.

When dark mode is enabled, the **Web** component enables the dark style defined in the media query **prefers-color-scheme** of the web page. If it is not defined, the web page remains unchanged. To enable forcible dark mode, use this API with [forceDarkAccess](#forcedarkaccess). For details about how to use dark mode, see [Setting Dark Mode](../../../web/web-set-dark-mode.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebDarkMode](arkts-arkweb-webdarkmode-e.md) | Yes | Dark mode for the web page, which can be set to **Off**, **On**, or **Auto**. When **null** or **undefined** is passed, the value is **WebDarkMode.Off**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: WebDarkMode = WebDarkMode.On;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .darkMode(this.mode)
    }
  }
}
```

## databaseAccess

```TypeScript
databaseAccess(databaseAccess: boolean)
```

Sets whether to enable the Web SQL Database storage API permission. If this permission is not explicitly called, it is disabled by default.

> **NOTE：**
> 
> - After the ArkWeb kernel is upgraded to M132, the API's control over the Web SQL Database becomes invalid
> because the kernel discards Web SQL. For details about the ArkWeb kernel version, see
> [Constraints](../../../web/web-component-overview.md#constraints).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| databaseAccess | boolean | Yes | Whether to enable Web SQL Database storage API permission.    **true** means enabling the detection, and **false** means disabling it. If **undefined** or **null** is passed in, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .databaseAccess(true)
    }
  }
}
```

## dataDetectorConfig

```TypeScript
dataDetectorConfig(config: TextDataDetectorConfig)
```

Configures text recognition settings.

This API must be used together with [enableDataDetector](#enabledatadetector). It takes effect only when **enableDataDetector** is set to **true**.

When entities A and B overlap, the following rules are followed:

1. If A is a subset of B (A ⊂ B), then B is retained; otherwise, A is retained.
2. If A is not a subset of B (A ⊄ B) and B is not a subset of A (B ⊄ A), and if the starting point of A is earlier
than that of B (A.start &lt; B.start), then A is retained; otherwise, B is retained.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [TextDataDetectorConfig](../../apis-arkui/arkts-apis/arkts-arkui-textdatadetectorconfig-i.md) | Yes | Text recognition configuration. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableDataDetector(true)
        .dataDetectorConfig({
          types: [
            TextDataDetectorType.PHONE_NUMBER,
            TextDataDetectorType.EMAIL
          ],
          color: Color.Red,
          decoration: {
            type: TextDecorationType.LineThrough,
            color: Color.Green,
            style: TextDecorationStyle.WAVY
          }
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Example dataDetectorConfig</title>;
</head>
<body>
    <p> Telephone: 400-123-4567 </p>
    <p> Email: 12345678901@example.com </p>
    <p> Website: www.example.com (cannot be identified) </p>
</body>
</html>
```

## defaultFixedFontSize

```TypeScript
defaultFixedFontSize(size: number)
```

Sets the default fixed font size for the web page. For HTML elements that use the **monospace** font and do not specify **font-size**, the font size is rendered based on this value.

When this attribute is not explicitly called, the default fixed font size is **13**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | Default fixed font size to set, in px. Value range: [-2^31, 2^31-1]. In actual rendering, values greater than 72 px are handled as 72 px, and values less than 1 px are handled as 1 px. When **null** or **undefined** is passed in, the value is **13**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State fontSize: number = 16;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .defaultFixedFontSize(this.fontSize)
    }
  }
}
```

## defaultFontSize

```TypeScript
defaultFontSize(size: number)
```

Sets the default font size for the web page. For HTML elements that use non-monospace fonts and do not specify **font-size**, the font size is rendered based on this value.

When this attribute is not explicitly called, the default font size of the web page is **16**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | Default font size to set, in px. Value range: [-2^31, 2^31-1]. In actual rendering, values greater than 72 px are handled as 72 px, and values less than 1 px are handled as 1 px. When **null** or **undefined** is passed in, the value is **16**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State fontSize: number = 13;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .defaultFontSize(this.fontSize)
    }
  }
}
```

## defaultTextEncodingFormat

```TypeScript
defaultTextEncodingFormat(textEncodingFormat: string)
```

Sets the default text encoding format for the web page. When this attribute is not explicitly called, the default text encoding format of the web page is UTF-8.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textEncodingFormat | string | Yes | Default text encoding format. When **null** or **undefined** is passed in, the value is **UTF-8**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        // Set the height.
        .height(500)
        .defaultTextEncodingFormat("UTF-8")
        .javaScriptAccess(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width" />
    <title>My test html5 page</title>
</head>
<body>
    <p>Hello world!</p>
</body>
</html>
```

## domStorageAccess

```TypeScript
domStorageAccess(domStorageAccess: boolean)
```

Sets whether to enable the DOM Storage API permission. If this attribute is not explicitly called, the DOM Storage API permission is disabled by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domStorageAccess | boolean | Yes | Sets whether to enable the Document Object Model storage interface (DOM Storage API). The value **true** enables it, and **false** disables it. If **undefined** or **null** is passed, the default value **false** is used. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .domStorageAccess(true)
    }
  }
}
```

## editMenuOptions

```TypeScript
editMenuOptions(editMenu: EditMenuOptions)
```

Sets a custom text selection menu for the **Web** component.

> **NOTE：**
> 
> This API is similar to **bindSelectionMenu**, with the following differences:
> 
> - **editMenuOptions**: Adds extension items based on the system default menu style, with the trigger conditions
> unchanged.
> 
> - [bindSelectionMenu](#bindselectionmenu): Fully customizes the menu style and trigger
> conditions, as defined by the developer.
> 
> It is not recommended to use both at the same time. Choose based on the degree of customization required.
> You can use this attribute to customize a text menu.

You can use onCreateMenu to modify, add, and delete menu options. If you do not want to display the text menu, return an empty array.

You can use onMenuItemClick to customize the callback for menu options. This function is triggered after a menu option is clicked and determines whether to execute the default callback based on the return value. If **true** is returned, the system callback is not executed. If **false** is returned, the system callback is executed.

In [onPrepareMenu&lt;sup&gt;20+&lt;/sup&gt;](../../../reference/apis-arkui/arkui-ts/ts-text-common.md#properties-1), this callback is triggered after the text selection area changes and before the menu is displayed. You can modify, add, or delete menu options in the callback to dynamically update the menu.

If this method is used together with [selectionMenuOptions&lt;sup&gt;(deprecated)&lt;/sup&gt;](#selectionmenuoptions), the **selectionMenuOptions&lt;sup  
&gt; (deprecated) &lt;/sup&gt;** method does not take effect.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-editmenuoptions-i.md) | Yes | Custom text menu options for the Web component. The number of menu items, the content size, and the icon size are consistent with those of the ArkUI Menu component. Among the system-provided ID enum values ([TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md)) in the menu, only CUT, COPY, PASTE, SELECT_ALL, TRANSLATE, SEARCH, and AI_WRITER are supported in the Web component. In the onMenuItemClick function, the textRange parameter is meaningless in the Web component, and the value passed in is -1. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

let selectText:string = '';
class TestClass {
  setSelectText(param: String) {
    selectText = param.toString();
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State testObj: TestClass = new TestClass();

  onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem> {
    let items = menuItems.filter((menuItem) => {
      // Filter the menu items as required.
      return (
        menuItem.id.equals(TextMenuItemId.CUT) ||
        menuItem.id.equals(TextMenuItemId.COPY) ||
        menuItem.id.equals((TextMenuItemId.PASTE)) ||
        menuItem.id.equals((TextMenuItemId.TRANSLATE)) ||
        menuItem.id.equals((TextMenuItemId.SEARCH)) ||
        menuItem.id.equals((TextMenuItemId.AI_WRITER))
      )
    });
    let customItem1: TextMenuItem = {
      content: 'customItem1',
      id: TextMenuItemId.of('customItem1'),
      icon: $r('app.media.icon')
    };
    let customItem2: TextMenuItem = {
      content: $r('app.string.customItem2'),
      id: TextMenuItemId.of('customItem2'),
      icon: $r('app.media.icon')
    };
    items.push(customItem1);// Add an item to the end of the item list.
    items.unshift(customItem2);// Add an item to the beginning of the item list.

    return items;
  }

  onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
    if (menuItem.id.equals(TextMenuItemId.CUT)) {
      // Custom behavior
      console.info("Intercept ID: CUT")
      // The value **true** means intercepting this menu item and skipping the default system cut operation.
      return true;
    } else if (menuItem.id.equals(TextMenuItemId.COPY)) {
      // Custom behavior
      console.info("Not intercept ID: COPY")
      // The value **false** means not intercepting this menu item and performing the default system copy operation.
      return false;
    } else if (menuItem.id.equals(TextMenuItemId.of('customItem1'))) {
      // Custom behavior
      console.info("Intercept ID: customItem1")
      return true;// Custom menu item. If true is returned, the menu is not closed after being clicked. If false is returned, the menu is closed.
    } else if (menuItem.id.equals((TextMenuItemId.of($r('app.string.customItem2'))))){
      // Custom behavior
      console.info("Intercept ID: app.string.customItem2")
      return true;
    }
    return false;// Return the default value false.
  }

   onPrepareMenu = (menuItems: Array<TextMenuItem>) => {
    let item1: TextMenuItem = {
      content: 'prepare1',
      id: TextMenuItemId.of('prepareMenu1'),
    };
    let item2: TextMenuItem = {
      content: 'prepare2' + selectText,
      id: TextMenuItemId.of('prepareMenu2'),
    };
    menuItems.push(item1);// Add an item to the end of the item list.
    menuItems.unshift(item2);// Add an item to the beginning of the item list.

    return menuItems;
  }

  @State EditMenuOptions: EditMenuOptions =
    { onCreateMenu: this.onCreateMenu, onMenuItemClick: this.onMenuItemClick, onPrepareMenu:this.onPrepareMenu }

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .editMenuOptions(this.EditMenuOptions)
        .javaScriptProxy({
          object: this.testObj,
          name: "testObjName",
          methodList: ["setSelectText"],
          controller: this.controller,
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>editMenuOptions Demo</h1>
    <span>edit menu options</span>
    <script>
      document.addEventListener('selectionchange', () => {
        var selection = window.getSelection();
        if (selection.rangeCount > 0) {
          var selectedText = selection.toString();
          testObjName.setSelectText(selectedText);
        }
      });
  </script>
  </body>
</html>
```

## enableAutoFill

```TypeScript
enableAutoFill(value: boolean)
```

Sets whether to enable web page autofill. By default, this feature is enabled.

<!--RP1-->

> **NOTE：**
> 
> The autofill feature of this API depends on SmartFill service and Password Autofill Service.

<!--RP1End-->

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to enable autofill for web pages. The value **true** means to enable autofill, and **false** means the opposite. When **undefined** or **null** is passed in, the value is **true**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableAutoFill(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0;" name="viewport"/>
    <title>Autofill test</title>
  </head>
  <body>
    <h4 align="center">Autofill test</h4>
    <form method="post" action="">
      <div align="center">
        <label for="name" style="width: 120px; display: inline-block; text-align: end;">Name:</label>
        <input type="text" id="name" autocomplete="name"/><br/><br/>
        <label for="tel-national" style="width: 120px; display: inline-block; text-align: end;">Mobile number:</label>
        <input type="text" id="tel-national" autocomplete="tel-national"/><br/><br/>
      </div>
      <div align="center">
        <button type="submit" style="width: 80px">Submit</button>
      </div>
    </form>
  </body>
</html>
```

## enableDataDetector

```TypeScript
enableDataDetector(enable: boolean)
```

Sets whether to recognize special entities of web texts, such as emails, phone numbers, and URLs. This API depends on the text recognition capability at the bottom layer of the device. Otherwise, the setting is invalid. When this attribute is not explicitly called, the detector is disabled by default.

> **NOTE：**
> 
> Attributes such as [dataDetectorConfig](#datadetectorconfig) and
> [enableSelectedDataDetector](#enableselecteddatadetector) take effect only when this attribute
> is enabled.
> If **enableDataDetector** is set to **true** and [dataDetectorConfig](#datadetectorconfig) is
> not set, all types of entities will be recognized, and the **color** and **decoration** attributes of the
> recognized entities will be changed to the following styles:

<!--code_no_check-->

When **enableDataDetector** is set to **true** and [copyOptions](#copyoptions) is set to **CopyOptions.LocalDevice**, the AI menu feature is activated. In this case, after text is selected on the web page, the text selection menu can display the corresponding AI menu items, including **url** (open link), **email** (create new email), **phoneNumber** (call), **address** (navigate to the location), and **dateTime** (create new schedule reminder) from [TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md).

When the AI menu takes effect, the corresponding option can be displayed only when the selection contains a complete AI entity. This menu item and the askAI menu item in [TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md) do not appear at the same time.

For details about the application scenario, see [Using Smart Text Data Detector](../../../web/web-data-detector.md).

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether to enable web text recognition. The value **true** means to enable web text recognition, and **false** means the opposite. When **undefined** or **null** is passed in, the attribute setting does not take effect. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableDataDetector(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Example enableDataDetector</title>;
</head>
<body>
    <p> Telephone: 400-123-4567 </p>
    <p>Email: example@example.com </p>
</body>
</html>
```

## enableDefaultContextMenu

```TypeScript
enableDefaultContextMenu(enable: boolean)
```

Sets whether to enable the default right-click context menu. If this method is not explicitly called, the menu is disabled by default. The default menu supports only the **CUT**, **COPY**, **PASTE**, and **SELECT_ALL** menu items.

> **NOTE：**
> 
> - When the [onContextMenuShow](#oncontextmenushow) callback is set and returns **true** in the
> callback, the setting of this API does not take effect.
> 
> - The default menu items are controlled by [editMenuOptions](#editmenuoptions), through which
> you can customize the menu options.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether to enable the default right-click context menu. The value **true** means enabled, and **false** means disabled. When **undefined** or **null** is passed, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableDefaultContextMenu(true)
    }
  }
}
```

## enableDrag

```TypeScript
enableDrag(value: boolean)
```

Sets whether to enable the drag function. If this attribute is not explicitly called, the web page drag function is enabled by default.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to enable the web page drag function. The value **true** means enabled, and **false** means disabled. When **undefined** or **null** is passed, the value is **true**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  private controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('test.html'), controller: this.controller })
        .enableDrag(false)
    }
  }
}
```

HTML file to be loaded.

```TypeScript
<!--test.html-->
<!DOCTYPE html>
<html>
  <head><meta charset="UTF-8"><title>drag test</title></head>
  <body>
    <div id="drag" draggable="true" style="width:100px;height:100px;background:red;margin:20px;"></div>
    <div id="drop" style="width:200px;height:200px;background:gray;margin:20px;"></div>
    <script>
      drag.ondragstart=e=>e.dataTransfer.setData('text/plain','');
      drop.ondragover=e=>e.preventDefault();
      drop.ondrop=e=>{e.preventDefault(); drop.style.background='green';};
      drag.ondragend=()=>{drop.style.background='gray';};
    </script>
  </body>
</html>
```

## enableFollowSystemFontWeight

```TypeScript
enableFollowSystemFontWeight(follow: boolean)
```

Sets whether the **Web** component can change the font weight according to the system settings. When this attribute is not explicitly called, the **Web** component can't change the font weight according to the system settings by default.

> **NOTE：**
> 
> Currently, only front-end text elements support this capability. The **canvas** element and embedded .docx and
> .pdf texts do not support this capability.

**Since:** 18

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| follow | boolean | Yes | Whether the **Web** component can change the font weight according to the system settings. The value **true** means that the **Web** component can change the font weight according to the system settings, and **false** means the opposite. When **undefined** or **null** is passed in, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: "www.example.com", controller: this.controller })
        .enableFollowSystemFontWeight(true)
    }
  }
}
```

## enableFullscreenVideoOverlay

```TypeScript
enableFullscreenVideoOverlay(enabled: boolean)
```

Sets whether to enable the overlay fullscreen playback feature for the **Web** component. If this attribute is not explicitly called, this feature is disabled by default.

> **NOTE：**
> 
> - Currently, only videos in H.264 and H.265 decoding formats are supported.
> 
> - Only fullscreen requests initiated by video elements are responded to.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable the overlay fullscreen playback feature for the **Web** component.    **true** means the feature is enabled.    **false** means the feature is disabled. When **undefined** or **null** is passed, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      .enableFullscreenVideoOverlay(true)
    }
  }
}
```

## enableHapticFeedback

```TypeScript
enableHapticFeedback(enabled: boolean)
```

Sets whether to enable haptic feedback for number-pressed text in the **Web** component. The **ohos.permission.VIBRATE** permission must be declared. When this attribute is not explicitly called, haptic feedback is enabled by default.

**Since:** 13

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable vibration. The value **true** indicates that vibration is enabled, and **false** indicates the opposite. If **undefined** or **null** is passed, the default value is used, which means vibration is enabled. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
      .enableHapticFeedback(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>Test Web Page</title>
  </head>
  <body>
    <h1>enableHapticFeedback Demo</h1>
    <span>enable haptic feedback</span>
  </body>
</html>
```

## enableImageAnalyzer

```TypeScript
enableImageAnalyzer(enable: boolean)
```

Sets whether to enable AI analysis of web page images. Currently, the image text recognition feature is supported. If this attribute is not explicitly called, this feature is enabled by default.

> **NOTE：**
> 
> When you number-press or hover the mouse over the image text, AI analyzer is triggered and the text in the image
> can be selected. The specifications of images that can trigger analyzer are as follows:
> 
> - The original width and height of the image are greater than or equal to 100 pixels.
> 
> - For [devices](../../../quick-start/module-configuration-file.md#devicetypes) other than 2-in-1 devices, the
> image rendering width must exceed 80% of the web page width.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether to enable AI analyzer for web page images. The value **true** means to enable AI analyzer, and **false** means the opposite. If **undefined** or **null** is passed in, the value is reset to **true**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableImageAnalyzer(true) // To disable the image analyzer, set this parameter to false.
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .image-container {
      width: 90%;
    }
    .image-container img {
      width: 100%;
      height: auto;
    }
  </style>
</head>
<body>
  <div class="image-container">
    <!--example.jpg is in the same directory as the HTML file-->
    <img src="example.jpg" alt="Image to be analyzed by AI">
  </div>
</body>
</html>
```

## enableMediaNetworkProxy

```TypeScript
enableMediaNetworkProxy(enabled: boolean)
```

Sets whether to enable the media resource network request proxy feature for the **Web** component. If this attribute is not explicitly called, this feature is disabled by default.

> **NOTE：**
> 
> - Currently, only HLS streaming media videos are supported.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable the media resource network request proxy feature for the **Web** component.    **true** means the feature is enabled.    **false** means the feature is disabled. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
      .enableMediaNetworkProxy(true)
    }
  }
}
```

## enableNativeEmbedMode

```TypeScript
enableNativeEmbedMode(enabled: boolean)
```

Sets whether to enable the same-layer rendering feature. When this method is not explicitly called, the same-layer rendering feature is disabled by default.

> **NOTE：**
> 
> APIs such as [registerNativeEmbedRule](#registernativeembedrule) and
> [nativeEmbedOptions](#nativeembedoptions) take effect only when this attribute is enabled.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to enable the same-layer rendering feature. The value **true** means to enable the same-layer rendering feature, and **false** means the opposite. When **undefined** or **null** is passed in, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeEmbedMode(true)
    }
  }
}
```

## enableNativeMediaPlayer

```TypeScript
enableNativeMediaPlayer(config: NativeMediaPlayerConfig)
```

Sets whether to enable the [application to take over web page media playback](../../../web/app-takeovers-web-media.md). When this attribute is not explicitly called, the web page media playback takeover feature is disabled by default.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [NativeMediaPlayerConfig](arkts-arkweb-nativemediaplayerconfig-i.md) | Yes | Configuration object for the app to take over web media playback. It contains the following attributes: enable (boolean type, whether to enable this feature, default value: false), shouldOverlay (boolean type, whether the player view of the app taking over web video playback overlays the web content after the feature is enabled, default value: false). If undefined or null is passed, it is equivalent to `{enable: false, shouldOverlay: false}`. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
    }
  }
}
```

## enableScrollDirectionalLock

```TypeScript
enableScrollDirectionalLock(value: boolean, type: ScrollDirectionalLockType)
```

Sets the scroll direction lock for the **Web** component to prevent simultaneous horizontal and vertical scrolling when the user swipes diagonally, thereby improving the scrolling experience. If this method is not explicitly called, scroll direction lock is supported by default in nested scrolling scenarios. The **ALL** mode applies to all scenarios where scroll locking is needed, while the **NESTED_SCROLL** mode applies only to nested scrolling scenarios.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to enable scroll direction lock. The value **true** means the scroll direction is locked, and the scroll view locks the scroll axis based on the user's initial swipe direction. The value **false** means no locking. |
| type | [ScrollDirectionalLockType](arkts-arkweb-scrolldirectionallocktype-e.md) | Yes | Specifies the scenarios in which the **Web** component applies scroll direction lock. **ALL** means scroll lock is supported in all scenarios, and **NESTED_SCROLL** means scroll lock is supported in nested scrolling scenarios. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .width('100%')
        .height('100%')
        // Supports locking of the scroll direction in all scenarios.
        .enableScrollDirectionalLock(true, ScrollDirectionalLockType.ALL)
    }
  }
}
```

## enableSelectedDataDetector

```TypeScript
enableSelectedDataDetector(enable: boolean)
```

Sets whether to enable the AI menu feature for text selection menu. After the AI menu feature is enabled, the email, phone number, website, date, and address in the selection can be identified, and the corresponding AI menu items are displayed in the text selection menu. By default, the AI menu feature is enabled.

When the AI menu feature is enabled, after text is selected on the web page, the text selection menu can display the corresponding AI menu items, including **url** (open link), **email** (create new email), **phoneNumber** (call), **address** (navigate to the location), and **dateTime** (create new schedule) from [TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md).

When the AI menu takes effect, the corresponding option can be displayed only when the selection contains a complete AI entity. This menu item and the askAI menu item in [TextMenuItemId](../../apis-arkui/arkts-apis/arkts-arkui-textmenuitemid-c.md) do not appear at the same time.

For details about the application scenario, see [Using Smart Text Data Detector](../../../web/web-data-detector.md).

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether to enable web text recognition. The value **true** means to enable web text recognition, and **false** means the opposite. If **undefined** or **null** is passed in, the attribute is reset to the default value. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableSelectedDataDetector(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>enableSelectedDataDetector Example</title>
</head>
<body>
    <p> Telephone: 400-123-4567 </p>
    <p>Email: example@example.com </p>
</body>
</html>
```

## enableWebAVSession

```TypeScript
enableWebAVSession(enabled: boolean)
```

Sets whether to support an application to connect to media controller. If this attribute is not explicitly set, the application can connect to media controller by default.

**Since:** 18

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether to support an application to connect to media controller. The value **true** means to support an application to connect to media controller, and **false** means the opposite. When **undefined** or **null** is passed in, the value is **true**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .enableWebAVSession(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Video Playback Page</title>
</head>
<body>
    <h1>Video Playback</h1>
    <video id="testVideo" controls>
        <!--Save an MP4 media file in the rawfile directory of resources and name it example.mp4.-->
        <source src="example.mp4" type="video/mp4">
    </video>
</body>
</html>
```

## fileAccess

```TypeScript
fileAccess(fileAccess: boolean)
```

Sets whether to enable access to the file system in the application. This setting does not affect the access to the files specified through [\$rawfile(filepath/filename)](../../../quick-start/resource-categories-and-access.md#accessing-resources). For API version 11 and earlier versions, access to the file system in the application is enabled by default if this attribute is not explicitly called. Since API version 12, access to the file system in the application is disabled by default if this attribute is not explicitly called.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fileAccess | boolean | Yes | Whether to enable access to the file system in the app. The value **true** means to enable, and **false** means to disable. In addition, when fileAccess is **false**, resources in the read-only resource directory `/data/storage/el1/bundle/entry/resources/resfile` can still be accessed through the file protocol, which is not controlled by fileAccess. In API version 11 and earlier, the value is **true** when undefined or null is passed. In API version 12 and later, the value is **false** when undefined or null is passed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .fileAccess(true)
    }
  }
}
```

## forceDarkAccess

```TypeScript
forceDarkAccess(access: boolean)
```

Sets whether to enable forcible dark mode for the web page. This API is applicable only when [darkMode](#darkmode) is enabled. When this attribute is not explicitly called, forcible dark mode is disabled for the web page by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| access | boolean | Yes | Whether to enable forced dark mode for web pages. The value **true** means to enable it, and **false** means not to enable it. If null or undefined is passed, the default value **false** is used. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: WebDarkMode = WebDarkMode.On;
  @State access: boolean = true;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .darkMode(this.mode)
        .forceDarkAccess(this.access)
    }
  }
}
```

## forceDisplayScrollBar

```TypeScript
forceDisplayScrollBar(enabled: boolean)
```

Sets whether the scroll bar is always visible. Under the always-visible settings, when the page size exceeds one page, the scroll bar appears and remains visible. When this attribute is not explicitly called, the scroll bar is not always visible by default.

When **layoutMode** is set to **WebLayoutMode.FIT_CONTENT**, the **enabled** parameter is set to **false**.

> **NOTE：**
> 
> - This interface takes effect globally across all web components in the current application. When multiple web
> components are set with different values, the value set for the first time will be used.
> 
> - It is recommended that you use
> [setScrollbarMode](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#setscrollbarmode) to set the scrollbar
> mode for all web components currently applied. If the setScrollbarMode interface is invoked at the same time,
> the setting of the forceDisplayScrollBar interface does not take effect.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether the scroll bar is always displayed. The value **true** indicates that the scroll bar is always displayed, and **false** indicates the opposite. When layoutMode is set to WebLayoutMode.FIT_CONTENT, the enabled parameter is forcibly set to **false**, and setting it to **true** does not take effect. If **undefined** or **null** is passed in, the attribute setting does not take effect. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .forceDisplayScrollBar(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <style>
      body {
        width:2560px;
        height:2560px;
        padding-right:170px;
        padding-left:170px;
        border:5px solid blueviolet;
      }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## forceEnableZoom

```TypeScript
forceEnableZoom(enable: boolean)
```

Sets whether to enable the forcible zoom functionality for the **Web** component.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Whether to comply with the zoom restriction specified by the **&lt;meta name="viewport"&gt;** tag on the web page. The value **true** means to not comply with the web page zoom restriction, and **false** means the opposite. When **undefined** or **null** is passed in, the attribute setting does not take effect. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .forceEnableZoom(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
  <title>Test Web Page</title>
</head>
<body>
  <h1>forceEnableZoom Demo</h1>
  <span>You can scale page when forceEnableZoom is true.</span>
</body>
</html>
```

## geolocationAccess

```TypeScript
geolocationAccess(geolocationAccess: boolean)
```

Sets whether to enable the geolocation permission. If this attribute is not explicitly called, the permission is enabled by default. For details about how to use this feature, see [Managing Location Permissions](../../../web/web-geolocation-permission.md).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| geolocationAccess | boolean | Yes | Whether to enable the geolocation permission. The value **true** means to enable the permission, and **false** means the opposite. The value **false** is used when **undefined** or **null** is passed in. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .geolocationAccess(true)
    }
  }
}
```

## gestureFocusMode

```TypeScript
gestureFocusMode(mode: GestureFocusMode)
```

Sets the gesture focus mode of the **Web** component, which controls the focus response behavior of the **Web** component. If this attribute is not explicitly called, the default behavior is that any gesture causes the **Web** component to gain focus when the gesture is pressed.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [GestureFocusMode](arkts-arkweb-gesturefocusmode-e.md) | Yes | Gesture focus mode of the **Web** component. If **undefined** or **null** is passed in, the value **GestureFocusMode.DEFAULT** is used. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: GestureFocusMode = GestureFocusMode.DEFAULT;
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .gestureFocusMode(this.mode)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <input type="text" placeholder="Text">
</body>
</html>
```

## horizontalScrollBarAccess

```TypeScript
horizontalScrollBarAccess(horizontalScrollBar: boolean)
```

Sets whether to display the horizontal scrollbar, including the system default scrollbar and user-defined scrollbars. If this attribute is not explicitly called, the scrollbar is displayed by default.

> **NOTE：**
> 
> - If an [@State](../../../ui/state-management/arkts-state.md) decorated variable is used to control the
> visibility of the horizontal scrollbar,
> [controller.refresh()](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#refresh) must be called for the
> settings to take effect.
> 
> - When the [@State](../../../ui/state-management/arkts-state.md) decorated variable changes frequently and
> dynamically, it is recommended to maintain a one-to-one correspondence between the toggle variable and the
> **Web** component.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontalScrollBar | boolean | Yes | Sets whether to display the horizontal scrollbar. The value **true** indicates to display it, and **false** indicates not to display it. The default value is **false** when undefined or null is passed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State isShow: boolean = true;
  @State btnMsg: string = 'Hide scrollbar';

  build() {
    Column() {
      // If an @State decorated variable is used to control the horizontal scrollbar visibility, controller.refresh() must be called for the settings to take effect.
      Button('refresh')
        .onClick(() => {
          if (this.isShow) {
            this.isShow = false;
            this.btnMsg = 'Show scrollbar';
          } else {
            this.isShow = true;
            this.btnMsg = 'Hide scrollbar';
          }
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`Failed to refresh Web. Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
          }
        }).height('10%').width('40%')
      Web({ src: $rawfile('index.html'), controller: this.controller }).height('90%')
        .horizontalScrollBarAccess(this.isShow)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
    <title>Demo</title>
    <style>
        body {
          width:3000px;
          height:6000px;
          padding-right:170px;
          padding-left:170px;
          border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## imageAccess

```TypeScript
imageAccess(imageAccess: boolean)
```

Sets whether to allow automatic loading of image resources. If this attribute is not explicitly called, automatic loading is allowed by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageAccess | boolean | Yes | Whether to allow automatic loading of image resources. The value **true** means allowed, and **false** means not allowed. If **undefined** or **null** is passed, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .imageAccess(true)
    }
  }
}
```

## initialScale

```TypeScript
initialScale(percent: number)
```

Sets the zoom percentage of the entire page. If this attribute is not explicitly called, the default value is **100**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| percent | number | Yes | Scale factor of the entire page. Value range: (0, 1000] When **undefined** or **null** is passed in, the attribute setting does not take effect. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State percent: number = 100;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .initialScale(this.percent)
    }
  }
}
```

## javaScriptAccess

```TypeScript
javaScriptAccess(javaScriptAccess: boolean)
```

Sets whether to allow execution of JavaScript scripts. If this attribute is not explicitly called, execution is allowed by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| javaScriptAccess | boolean | Yes | Whether to allow JavaScript script execution. The value **true** means allowed, and **false** means not allowed. The default value is **false** when undefined or null is passed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .javaScriptAccess(true)
    }
  }
}
```

## javaScriptOnDocumentEnd

```TypeScript
javaScriptOnDocumentEnd(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the specified page or document has been loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**
> 
> - The script runs after any JavaScript code on the page, and the DOM tree has already been loaded and rendered at
> that point.
> 
> - The scripts are executed in lexicographic order, not in the order of the array.
> 
> - When scripts with identical content are injected multiple times, they are silently deduplicated without display
> or notification, and the **scriptRules** from the first injection are used.
> 
> - This API does not support [UrlRegexRule](arkts-arkweb-urlregexrule-i.md).
> 
> - You are advised to use [runJavaScriptOnDocumentEnd](#runjavascriptondocumentend) instead.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes | Script item array to be injected. When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  private jsStr: string =
    "window.document.getElementById(\"result\").innerHTML = 'this is msg from javaScriptOnDocumentEnd'";
  @State scripts: Array<ScriptItem> = [
    { script: this.jsStr, scriptRules: ["*"] }
  ];

  build() {
    Column({ space: 20 }) {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .backgroundColor(Color.Grey)
        .javaScriptOnDocumentEnd(this.scripts)
        .width('100%')
        .height('100%')
    }
  }
}
```

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;">
Hello world!
<div id="result">test msg</div>
</body>
</html>
```

## javaScriptOnDocumentStart

```TypeScript
javaScriptOnDocumentStart(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the specified page or document starts to be loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**
> 
> - The script is injected after the root element (HTML Element) of the web document is created but before any
> other content is loaded.
> 
> - The scripts are executed in lexicographic order, not in the order of the array. If the original array order is
> required, use the [runJavaScriptOnDocumentStart](#runjavascriptondocumentstart) API instead.
> 
> - When scripts with identical content are injected multiple times, they are silently deduplicated without display
> or notification, and the **scriptRules** from the first injection are used.
> 
> - This API does not support [UrlRegexRule](arkts-arkweb-urlregexrule-i.md).
> 
> - You are advised to use [runJavaScriptOnDocumentStart](#runjavascriptondocumentstart) instead.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes | Script item array to be injected. When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components. |

## javaScriptProxy

```TypeScript
javaScriptProxy(javaScriptProxy: JavaScriptProxy)
```

Registers the ArkTS object in **javaScriptProxy** with the **Web** component. The object will be registered in all frames of the web page, including all iframes, using the name specified in **JavaScriptProxy**. This enables JavaScript to call methods of the ArkTS object in **javaScriptProxy**.

> **NOTE：**
> 
> The **javaScriptProxy** API must be used together with
> [deleteJavaScriptRegister&lt;sup&gt;9+&lt;/sup&gt;](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#deletejavascriptregister)
> to prevent memory leaks.
> 
> All parameters of the **javaScriptProxy** object cannot be updated.
> 
> When registering a **javaScriptProxy** object, at least one of the synchronous or asynchronous method lists must
> be non-empty. Both types of methods can be registered simultaneously.
> 
> This API supports registering only one object. To register multiple objects, use
> [registerJavaScriptProxy&lt;sup&gt;9+&lt;/sup&gt;](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#registerjavascriptproxy).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| javaScriptProxy | [JavaScriptProxy](arkts-arkweb-javascriptproxy-i.md) | Yes | Object to be registered. Methods can be declared, but attributes cannot. When **undefined** or **null** is passed in, the ArkTS object in javaScriptProxy is not registered with the **Web** component.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class TestObj {
  constructor() {
  }

  test(data1: string, data2: string, data3: string): string {
    console.info("data1:" + data1);
    console.info("data2:" + data2);
    console.info("data3:" + data3);
    return "AceString";
  }

  asyncTest(data: string): void {
    console.info("async data:" + data);
  }

  toString(): void {
    console.info('toString' + "interface instead.");
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  testObj = new TestObj();
  build() {
    Column() {
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .javaScriptAccess(true)
        .javaScriptProxy({
          object: this.testObj,
          name: "objName",
          methodList: ["test", "toString"],
          asyncMethodList: ["asyncTest"],
          controller: this.controller,
      })
    }
  }
}
```

## keyboardAppearance

```TypeScript
keyboardAppearance(mode: WebKeyboardAppearanceMode)
```

Sets the keyboard appearance mode, which controls the appearance style of the keyboard that pops up for input boxes in the **Web** component, including immersive and non-immersive modes. If this method is not explicitly called, the system immersive mode is followed by default.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebKeyboardAppearanceMode](arkts-arkweb-webkeyboardappearancemode-e.md) | Yes | Keyboard appearance. When **undefined** or **null** is passed, the system immersive mode is followed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State appearanceMode: WebKeyboardAppearanceMode = WebKeyboardAppearanceMode.DARK_IMMERSIVE;

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
      .keyboardAppearance(this.appearanceMode)
    }
  }
}
```

HTML file to be loaded.

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>test page</title>
</head>
<body>
  <input type="text" placeholder="Text">
</body>
</html>
```

## keyboardAvoidMode

```TypeScript
keyboardAvoidMode(mode: WebKeyboardAvoidMode)
```

Sets the custom soft keyboard avoidance mode.

If the keyboard avoidance mode set in **UIContext** is [KeyboardAvoidMode.RESIZE](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md), this API does not take effect.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebKeyboardAvoidMode](arkts-arkweb-webkeyboardavoidmode-e.md) | Yes | Web soft keyboard avoidance mode. In the nested scrolling scenario, the soft keyboard avoidance mode of the **Web** component is not recommended, including **RESIZE_VISUAL** and **RESIZE_CONTENT**. Default value: **WebKeyboardAvoidMode.RESIZE_CONTENT |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State avoidMode: WebKeyboardAvoidMode = WebKeyboardAvoidMode.RESIZE_VISUAL;

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
      .keyboardAvoidMode(this.avoidMode)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <input type="text" placeholder="Text">
</body>
</html>
```

## layoutMode

```TypeScript
layoutMode(mode: WebLayoutMode)
```

Sets the layout mode of the **Web** component. If this attribute is not explicitly called, the **Web** layout follows the system mode (**WebLayoutMode.NONE**) by default. For common issues, see [Web Component Size Adapting to Page Content Layout](../../../web/web-fit-content.md).

> **NOTE：**
> 
> Currently, only two **Web** layout modes are supported:
> 
> - The **Web** layout follows the system mode (**WebLayoutMode.NONE**).
> 
> - The **Web** component height adapts to the frontend page height (**WebLayoutMode.FIT_CONTENT**).
> 
> The adaptive layout of the **Web** component height based on the frontend page has the following limitations:
> 
> - When **layoutMode** is set to **WebLayoutMode.FIT_CONTENT**:
> 
> - [forceDisplayScrollBar](#forcedisplayscrollbar) does not support persistent display.
> 
> - [blankScreenDetectionConfig](#blankscreendetectionconfig) does not take effect.
> 
> - If the width or height of the **Web** component exceeds 7680 px, specify the **RenderMode.SYNC_RENDER** mode
> when creating the **Web** component. Otherwise, the entire screen will be blank.
> 
> - Dynamic switching of the **layoutMode** mode is not supported after the **Web** component is created.
> 
> - **Web** component size specifications: When **RenderMode.ASYNC_RENDER** is specified, the width and height must
> not exceed 7680 px respectively.
> 
> - Frequent changes to the page width and height will trigger re-layout of the **Web** component, affecting the
> user experience.
> 
> - Waterfall layout web pages (loading more content when scrolling to the bottom) are not supported.
> 
> - Width adaptation is not supported; only height adaptation is supported.
> 
> - Because the height adapts to the web page height, you cannot modify the component height by changing the
> component height attribute.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebLayoutMode](arkts-arkweb-weblayoutmode-e.md) | Yes | Specifies the Web layout mode, which can follow the system or adaptive layout. When null or undefined is passed, `WebLayoutMode.NONE` is used. |

**Examples**

After specifying the layoutMode to WebLayoutMode.FIT_CONTENT, you need to explicitly specify the renderMode to RenderMode.SYNC_RENDER. Otherwise, rendering errors may occur when the viewport height exceeds 7680 px in the default RenderMode.ASYNC_RENDER.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  mode: WebLayoutMode = WebLayoutMode.FIT_CONTENT;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller, renderMode: RenderMode.SYNC_RENDER })
        .layoutMode(this.mode)
    }
  }
}
```

After specifying the layoutMode to WebLayoutMode.FIT_CONTENT, you are advised to specify [overScrollMode](#overscrollmode) to OverScrollMode.NEVER. Otherwise, when the web page scrolls to the edge in the nested scrolling scenario, the rebounding effect is triggered first, which affects user experience.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  layoutMode: WebLayoutMode = WebLayoutMode.FIT_CONTENT;
  @State overScrollMode: OverScrollMode = OverScrollMode.NEVER;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller, renderMode: RenderMode.SYNC_RENDER })
        .layoutMode(this.layoutMode)
        .overScrollMode(this.overScrollMode)
    }
  }
}
```

## mediaOptions

```TypeScript
mediaOptions(options: WebMediaOptions)
```

Sets the web-based media playback policy, including the validity period for automatically resuming a paused web audio, and whether the audio of multiple **Web** instances in an application is exclusive. When this attribute is not explicitly set, the web audio cannot be automatically resumed after regaining the focus by default, and the audio of multiple **Web** instances in an application is exclusive.

> **NOTE：**
> 
> - Audios in the same **Web** instance are considered as the same audio.
> 
> - The media playback policy controls videos with an audio track.
> 
> - You are advised to set [audioExclusive](arkts-arkweb-webmediaoptions-i.md) to the same value for all **Web** components.
> 
> - Audio and video interruption takes effect within an application and between applications, and playback
> resumption takes effect only between applications.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WebMediaOptions](arkts-arkweb-webmediaoptions-i.md) | Yes | Web-based media playback policy. After the parameter settings are updated, the playback must be started again for the settings to take effect. When **undefined** or **null** is passed in, **{resumeInterval: 0, audioExclusive: true}** is used. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State options: WebMediaOptions = {resumeInterval: 10, audioExclusive: true};

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .mediaOptions(this.options)
    }
  }
}
```

## mediaPlayGestureAccess

```TypeScript
mediaPlayGestureAccess(access: boolean)
```

Sets whether autoplay of audible videos requires a user tap. Muted video playback is not affected by this API. If this attribute is not explicitly set, a user tap is required by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| access | boolean | Yes | Whether the autoplay of videos with audio requires a user tap. The value **true** indicates that a user tap is required, and **false** indicates that the video can be autoplayed. If **undefined** or **null** is passed, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State access: boolean = true;

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .mediaPlayGestureAccess(this.access)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Video Playback Page</title>
</head>
<body>
<h1>Video Playback</h1>
<video id="testVideo" controls autoplay>
    // Configure the autoplay attribute in the video tag to allow automatic video playback.
    // Save an MP4 media file in the rawfile directory of resources and name it example.mp4.
    <source src="example.mp4" type="video/mp4">
</video>
</body>
</html>
```

## metaViewport

```TypeScript
metaViewport(enabled: boolean)
```

Sets whether the **viewport** attribute of the **meta** tag is enabled. When this attribute is not explicitly called, the **viewport** attribute of the **meta** tag is supported by default.

> **NOTE：**
> 
> - Whether the **viewport** attribute of the **\&lt;meta&gt;** tag in the frontend HTML page is enabled is determined by
> checking whether the User-Agent contains the "Mobile" field. When the User-Agent does not contain the "Mobile"
> field, the **viewport** attribute in the **\&lt;meta&gt;** tag is disabled by default. In this case, you can explicitly
> set the **metaViewport** attribute to **true** to override the disabled state.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean | Yes | Whether the **viewport** attribute of the **meta** tag is enabled. The value **true** indicates that the **viewport** attribute of the **meta** tag is enabled and parsed, and the layout is performed based on the **viewport** attribute. The value **false** indicates the **viewport** attribute of the **meta** tag is disabled and not parsed, and the default layout is used. When **null** or **undefined** is passed in, the value is **true**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .metaViewport(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <p>Hello world!</p>
</body>
</html>
```

## minFontSize

```TypeScript
minFontSize(size: number)
```

Sets the minimum font size for the web page. If the font size of HTML elements is smaller than the value set by this API, the font size is rendered based on the value set by this API.

When no attribute is explicitly called, the default minimum font size of the web page is **8**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | Minimum font size to set, in px. Value range: [-2^31, 2^31-1]. In actual rendering, values greater than 72 px are handled as 72 px, and values less than 1 px are handled as 1 px. When **null** or **undefined** is passed in, the value is **8**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State fontSize: number = 13;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .minFontSize(this.fontSize)
    }
  }
}
```

## minLogicalFontSize

```TypeScript
minLogicalFontSize(size: number)
```

Sets the minimum logical font size for the web page.

For HTML elements whose font size is not specified:

1. If the font size of the element is smaller than the value set by this API, the font size is rendered based on the API value.
2. If **minLogicalFontSize** and **minFontSize** are both set, the larger value of the two will be used for elements whose font size is not specified.

When this attribute is not explicitly called, the default minimum logical font size of the web page is **8**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | number | Yes | Sets the minimum logical font size for web pages, in px. The value ranges from [-2^31, 2^31-1]. During actual rendering, values greater than 72 px are rendered as 7 2 px, and values less than 1 px are rendered as 1 px. Defaults to 8 when null or undefined is passed in. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State fontSize: number = 13;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .minLogicalFontSize(this.fontSize)
    }
  }
}
```

## mixedMode

```TypeScript
mixedMode(mixedMode: MixedMode)
```

Sets the behavior when a secure source attempts to load resources from an insecure source. When this attribute is not explicitly called, the default value is **MixedMode.None**, which means that secure sources are not allowed to load content from insecure sources.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mixedMode | [MixedMode](arkts-arkweb-mixedmode-e.md) | Yes | Mixed content mode to be set. If **undefined** or **null** is passed in, the value **MixedMode.All** is used. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: MixedMode = MixedMode.All;
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .mixedMode(this.mode)
    }
  }
}
```

## multiWindowAccess

```TypeScript
multiWindowAccess(multiWindow: boolean)
```

Sets whether to enable the multi-window permission. If this attribute is not explicitly called, the permission is disabled by default.

Enabling the multi-window permission requires implementation of the **onWindowNew** event. For the sample code, see [onWindowNew](#onwindownew).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| multiWindow | boolean | Yes | Whether to enable the multi-window permission. The value **true** means to enable, and **false** means the opposite. |

## nativeEmbedOptions

```TypeScript
nativeEmbedOptions(options?: EmbedOptions)
```

Sets the same-layer rendering configuration. This attribute takes effect only when [enableNativeEmbedMode](#enablenativeembedmode) is enabled and cannot be dynamically modified. If this attribute is not explicitly called, the default value **{supportDefaultIntrinsicSize: false}** is used.

**Since:** 16

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EmbedOptions](arkts-arkweb-embedoptions-i.md) | No | Configuration options of the same-layer rendering. If **undefined** or **null** is passed in, the value **{supportDefaultIntrinsicSize: false}** is used. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  options: EmbedOptions = {supportDefaultIntrinsicSize: true};

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableNativeEmbedMode(true)
        .nativeEmbedOptions(this.options)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendered Fixed-Size HTML Test</title>
</head>
<body>
<div>
    <embed id="input" type = "native/view" style = "background-color:red"/>
</div>
</body>
</html>
```

## nestedScroll

```TypeScript
nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt)
```

Sets nested scrolling options.

> **NOTE：**
> 
> - You can set the up, down, left, and right directions, or set the forward and backward nested scrolling modes to
> implement scrolling linkage with the parent component.
> 
> - Containers that support nested scrolling: Grid, List, Scroll,
> Swiper, Tabs, WaterFlow, Refresh and
> [bindSheet](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md#bindsheet).
> 
> - Input sources that support nested scrolling: gestures, mouse device, and touchpad.
> 
> - In nested scrolling scenarios, since the **Web** component's over-scrolling to the edge will trigger the over-
> scroll bounce effect first, it is recommended that you set [overScrollMode](#overscrollmode) to
> **OverScrollMode.NEVER** to avoid undermining user experience.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| [NestedScrollOptionsExt](arkts-arkweb-nestedscrolloptionsext-i.md) | Yes | Nested scrolling options. When the value is of the **NestedScrollOptions** type (forward and backward), the default nested scrolling mode of the **scrollForward** and **scrollBackward** options is [NestedScrollMode.SELF_FIRST](../../apis-arkui/arkts-apis/arkts-arkui-nestedscrollmode-e.md). When the value is of the **NestedScrollOptionsExt** type (up, down, left, and right), the default nested scrolling mode of the **scrollUp**, **scrollDown**, **scrollLeft**, and **scrollRight** options is **NestedScrollMode.SELF_FIRST**.<br>**Since:** 14 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .nestedScroll({
          scrollForward: NestedScrollMode.SELF_FIRST,
          scrollBackward: NestedScrollMode.SELF_FIRST,
        })
    }
  }
}
```

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  build() {
    Scroll(){
      Column() {
        Text("Nested Web")
          .height("25%")
          .width("100%")
          .fontSize(30)
          .backgroundColor(Color.Yellow)
        Web({ src: $rawfile('index.html'),
              controller: this.controller })
          .nestedScroll({
            scrollUp: NestedScrollMode.SELF_FIRST,
            scrollDown: NestedScrollMode.PARENT_FIRST,
            scrollLeft: NestedScrollMode.SELF_FIRST,
            scrollRight: NestedScrollMode.SELF_FIRST,
          })
      }
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .blue {
          background-color: lightblue;
        }
        .green {
          background-color: lightgreen;
        }
        .blue, .green {
        font-size:16px;
        height:200px;
        text-align: center;       /* Horizontally centered */
        line-height: 200px;       /* Vertically centered (the height matches the container height) */
        }
    </style>
</head>
<body>
<div class="blue" >webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
<div class="green">webArea</div>
<div class="blue">webArea</div>
</body>
</html>
```

## onActivateContent

```TypeScript
onActivateContent(callback: Callback<void>)
```

Triggered to check whether a bound **Web** instance exists based on the name when a web page triggers **window.open(url, name)**. If the instance exists, it receives this callback to notify the application of displaying it on the front end. If it does not exist, the application is notified to create a new **Web** instance through [onWindowNew](#onwindownew).

> **NOTE：**
> 
> - Binding a **Web** instance by name: Call the **event.handler.setWebController** method in the [onWindowNew] (#
> onwindownew9) callback and transfer the controller of the new **Web** instance.
> 
> - The name must comply with the regular expression **[a-zA-Z0-9_]+**. When the name is used as the value of the
> **target** attribute of the \&lt;a
&gt; or \&lt;form
&gt; tag, the bound **Web** instance also triggers this callback function.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;void&gt; | Yes | Callback triggered on a new page after **window.open** is triggered on the original page. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

// There are two Web components on the same page. When the WebComponent object opens a new window, the NewWebViewComp object is displayed.
@CustomDialog
struct NewWebViewComp {
  controller?: CustomDialogController;
  webviewController1: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: "https://www.example.com", controller: this.webviewController1 })
        .javaScriptAccess(true)
        .multiWindowAccess(false)
        .onWindowExit(() => {
          if (this.controller) {
            this.controller.close();
          }
        })
        .onActivateContent(() => {
          //The Web component needs to be displayed in the front. It is recommended that the application switch between tabs or windows to display the Web component.
          console.info("NewWebViewComp onActivateContent")
        })
    }.height("50%")
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  dialogController: CustomDialogController | null = null;

  build() {
    Column() {
      Web({ src: $rawfile("window.html"), controller: this.controller })
        .javaScriptAccess(true)
        .allowWindowOpenMethod(true)
        // MultiWindowAccess needs to be enabled.
        .multiWindowAccess(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController.close()
          }
          let popController: webview.WebviewController = new webview.WebviewController();
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController }),
            isModal: false
          })
          this.dialogController.open();
          // Return the WebviewController object corresponding to the new window to the web kernel.
          // If the event.handler.setWebController API is not called, the render process will be blocked.
          event.handler.setWebController(popController);
        })
    }
  }
}
```

```TypeScript
<!-- Code of the window.html page -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ActivateContentEvent</title>
</head>
<body>
<a href="#" onclick="openNewWindow('https://www.example.com')">Open a new page</a>
<script type="text/javascript">
    function openNewWindow(url) {
      window.open(url, 'example');
      return false;
    }
</script>
</body>
</html>
```

## onAdsBlocked

```TypeScript
onAdsBlocked(callback: OnAdsBlockedCallback)
```

Called after an ad is blocked on the web page to notify the user of detailed information about the blocked ad. To reduce the frequency of notifications and minimize the impact on the page loading process, only the first notification is made when the page is fully loaded. Subsequent blocking events are reported at intervals of 1 second, and no notifications are sent if there is no ad blocked.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnAdsBlockedCallback](arkts-arkweb-onadsblockedcallback-t.md) | Yes | Callback of **onAdsBlocked**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State totalAdsBlockCounts: number = 0;
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
      .onAdsBlocked((details: AdsBlockedDetails) => {
        if (details) {
          console.info(' Blocked ' + details.adsBlocked.length + ' in ' + details.url);
          let adList: Array<string> = Array.from(new Set(details.adsBlocked));
          this.totalAdsBlockCounts += adList.length;
          console.info('Total blocked counts :' + this.totalAdsBlockCounts);
        }
      })
    }
  }
}
```

## onAlert

```TypeScript
onAlert(callback: Callback<OnAlertEvent, boolean>)
```

Triggered when **alert()** is invoked to display an alert dialog box on the web page. Call the [handleCancel](arkts-arkweb-jsresult-c.md#handlecancel) or [handleConfirm](arkts-arkweb-jsresult-c.md#handleconfirm) API when this callback is triggered. Otherwise, the render process is blocked.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnAlertEvent](arkts-arkweb-onalertevent-i.md), boolean&gt; | Yes | Callback used when **alert()** is invoked to display an alert dialog box on the web page. Return value: boolean If the callback returns **true**, the application can use the custom dialog box (allows the confirm and cancel operations) and invoke the **JsResult** API to notify the **Web** component the confirmation result. If the callback returns **false**, the processing result of the dialog box is regarded as cancel.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onAlert((event) => {
          if (event) {
            console.info("event.url:" + event.url);
            console.info("event.message:" + event.message);
            this.uiContext.showAlertDialog({
              title: 'onAlert',
              message: 'text',
              primaryButton: {
                value: 'ok',
                action: () => {
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            })
          }
          return true;
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>WebView onAlert Demo</h1>
  <button onclick="myFunction()">Click here</button>
  <script>
    function myFunction() {
      alert("Hello World");
    }
  </script>
</body>
</html>
```

## onAudioStateChanged

```TypeScript
onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent>)
```

Triggered when the audio playback status on the web page changes.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnAudioStateChangedEvent](arkts-arkweb-onaudiostatechangedevent-i.md)&gt; | Yes | Callback invoked when the audio playback status on the web page changes. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State playing: boolean = false;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onAudioStateChanged(event => {
          this.playing = event.playing;
          console.info('onAudioStateChanged playing: ' + this.playing);
        })
    }
  }
}
```

## onBeforeUnload

```TypeScript
onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean>)
```

Called when the page refresh is about to complete or the current page is closed.

> **NOTE：**
> 
> - If the current **Web** component does not have the focus, **onBeforeUnload** is not triggered when the page is
> refreshed or closed.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnBeforeUnloadEvent](arkts-arkweb-onbeforeunloadevent-i.md), boolean&gt; | Yes | Callback triggered when the page refresh is about to complete or the current page is closed. Return value: boolean If the callback returns **true**, the application can use the custom dialog box (allows the confirm and cancel operations) and invoke the **JsResult** API to notify the **Web** component whether to exit the current page based on the user's operation. The value **false** means that the custom dialog box drawn in the function is ineffective.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onBeforeUnload((event) => {
          if (event) {
            console.info("event.url:" + event.url);
            console.info("event.message:" + event.message);
            console.info("event.isReload:" + event?.isReload ?? 'false');
            this.uiContext.showAlertDialog({
              title: 'onBeforeUnload',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  event.result.handleCancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            })
          }
          return true;
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body onbeforeunload="return myFunction()">
  <h1>WebView onBeforeUnload Demo</h1>
  <a href="https://www.example.com">Click here</a>
  <script>
    function myFunction() {
      return "onBeforeUnload Event";
    }
  </script>
</body>
</html>
```

## onCameraCaptureStateChange

```TypeScript
onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback)
```

Triggered to notify the user of the camera state on the current web page, which can be **None**, **Active**, or **Paused**. This API uses an asynchronous callback to return the result.

You can use the **startCamera**, **stopCamera**, and **closeCamera** APIs to enable, pause, and stop the camera respectively. For details about how to use them, see [startCamera](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#startcamera).

> **NOTE：**
> 
> **Active** is returned when the camera is being used on the current web page.
> 
> **Paused** is returned when the camera is paused on the current web page.
> 
> **None** is returned when the camera is not being used on the current web page.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnCameraCaptureStateChangeCallback](arkts-arkweb-oncameracapturestatechangecallback-t.md) | Yes | Callback triggered when the camera capture state changes. It returns the original and new states. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'], (err: BusinessError, data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    })
  }

  build() {
    Column() {
      Button("startCamera").onClick(() => {
        try {
          this.controller.startCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("stopCamera").onClick(() => {
        try {
          this.controller.stopCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("closeCamera").onClick(() => {
        try {
          this.controller.closeCamera();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
          }
        })
       .onCameraCaptureStateChange((event: CameraCaptureStateChangeInfo) => {
          console.info("CameraCapture from ", event.originalState, " to ", event.newState);
       })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
 <head>
   <meta charset="UTF-8">
 </head>
 <body>
   <video id="video" width="400px" height="400px" autoplay="autoplay">
   </video>
   <input type="button" title="HTML5 Camera" value="Enable Camera" onclick="getMedia()" />
   <script>
     function getMedia() {
       let constraints = {
         video: {
           width: 500,
           height: 500
         },
         audio: true
       }
       let video = document.getElementById("video");
       let promise = navigator.mediaDevices.getUserMedia(constraints);
       promise.then(function(MediaStream) {
         video.srcObject = MediaStream;
         video.play();
       })
     }
   </script>
 </body>
</html>
```

## onClientAuthenticationRequest

```TypeScript
onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent>)
```

Triggered when an SSL client certificate request is received.

> **NOTE：**
> 
> - The **Web** component can respond with
> [ClientAuthenticationHandler.confirm](arkts-arkweb-clientauthenticationhandler-c.md#confirm),
> [ClientAuthenticationHandler.cancel](arkts-arkweb-clientauthenticationhandler-c.md#cancel), or
> [ClientAuthenticationHandler.ignore](arkts-arkweb-clientauthenticationhandler-c.md#ignore).
> 
> - If **ClientAuthenticationHandler.confirm** or **ClientAuthenticationHandler.cancel** is called, the **Web**
> component stores the authentication result in the memory (within the application lifecycle) and does not call
> **onClientAuthenticationRequest()** again for the same host and port. If **onClientAuthenticationRequest.ignore**
> is called, the **Web** component does not store the authentication result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnClientAuthenticationEvent](arkts-arkweb-onclientauthenticationevent-i.md)&gt; | Yes | Callback invoked when an SSL client certificate is required.<br>**Since:** 12 |

**Examples**

Install a private credential to implement two-way authentication.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import { certificateManager } from '@kit.DeviceCertificateKit';
import { promptAction } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: WebviewController = new webview.WebviewController();
  uiContext : UIContext = this.getUIContext();
  context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
  uri: string = ''

  aboutToAppear(): void {
    webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
  }

  build() {
    Column() {
      Button("installPrivateCertificate").onClick(() => {
        if (!this.context) {
          return;
        }

        //Note: Replace badssl.com-client.p12 with the actual certificate file.
        let value: Uint8Array = this.context.resourceManager.getRawFileContentSync("badssl.com-client.p12");
        certificateManager.installPrivateCertificate(value, 'badssl.com', "1",
          async (err: BusinessError, data: certificateManager.CMResult) => {
            console.info(`installPrivateCertificate, uri==========${JSON.stringify(data.uri)}`)
            if (!err && data.uri) {
              this.uri = data.uri;
            }
          });
      })
      Button('Load the website that requires the client SSL certificate')
        .onClick(() => {
          this.controller.loadUrl("https://client.badssl.com")
        })
      Web({
        src: "https://www.bing.com/",
        controller: this.controller,
      }).domStorageAccess(true)
        .fileAccess(true)
        .onPageBegin(event => {
          console.info("extensions onpagebegin url " + event.url);
        })
        .onClientAuthenticationRequest((event) => {
          console.info("onClientAuthenticationRequest ");
          event.handler.confirm(this.uri);
          return true;
        })
        .onSslErrorEventReceive(e => {
          console.info(`onSslErrorEventReceive->${e.error.toString()}`);
        })
        .onErrorReceive((event) => {
          if (event) {
            this.getUIContext().getPromptAction().showToast({
              message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
              alignment: Alignment.Center
            })
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
            console.info('url:' + event.request.getRequestUrl());
          }
        })
        .onTitleReceive(event  => {
          console.info("title received " + event.title);
        })

    }
  }
}
```

Construct the singleton object GlobalContext.

```TypeScript
// GlobalContext.ets
export class GlobalContext {
  private constructor() {}
  private static instance: GlobalContext;
  private _objects = new Map<string, Object>();

  public static getContext(): GlobalContext {
    if (!GlobalContext.instance) {
      GlobalContext.instance = new GlobalContext();
    }
    return GlobalContext.instance;
  }

  getObject(value: string): Object | undefined {
    return this._objects.get(value);
  }

  setObject(key: string, objectClass: Object): void {
    this._objects.set(key, objectClass);
  }
}
```

Construct a CertManagerService object to interconnect with certificate management.

```TypeScript
// CertMgrService.ets
import { bundleManager, common, Want } from "@kit.AbilityKit";
import { BusinessError } from "@kit.BasicServicesKit";
import { GlobalContext } from './GlobalContext';

export default class CertManagerService {
  private static sInstance: CertManagerService;
  private authUri = "";
  private appUid = "";

  public static getInstance(): CertManagerService {
    if (CertManagerService.sInstance == null) {
      CertManagerService.sInstance = new CertManagerService();
    }
    return CertManagerService.sInstance;
  }

  async grantAppPm(): Promise<string> {
    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_DEFAULT | bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION;
    // Note: Replace com.example.myapplication with the actual application name.
    try {
      const data = await bundleManager.getBundleInfoForSelf(bundleFlags)
        .catch((err: BusinessError) => {
          console.error('getBundleInfoForSelf failed. Cause: %{public}s', err.message);
          return null;
        });
      this.appUid = data?.appInfo?.uid?.toString() ?? '';
      console.info('getBundleInfoForSelf successfully. Data: %{public}s', JSON.stringify(data));
    } catch (err) {
      let message = (err as BusinessError).message;
      console.error('getBundleInfoForSelf failed: %{public}s', message);
    }

    // Note: Add GlobalContext.getContext().setObject("AbilityContext", this.context) to the onCreate function in the MainAbility.ts file.
    let abilityContext = GlobalContext.getContext().getObject("AbilityContext") as common.UIAbilityContext;
    await abilityContext.startAbilityForResult(
      {
        bundleName: "com.ohos.certmanager",
        abilityName: "MainAbility",
        uri: "requestAuthorize",
        parameters: {
          appUid: this.appUid, // Pass the UID of the requesting application.
        }
      } as Want)
      .then((data: common.AbilityResult) => {
        if (!data.resultCode && data.want) {
          if (data.want.parameters) {
            this.authUri = data.want.parameters.authUri as string; // Obtain the returned authUri after successful authorization.
          }
        }
      })
    return this.authUri;
  }
}
```

Implement two-way authentication.

```TypeScript
import { webview } from '@kit.ArkWeb';
import CertManagerService from './CertMgrService';
import { promptAction } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  controller: WebviewController = new webview.WebviewController();
  certManager = CertManagerService.getInstance();

  aboutToAppear(): void {
    webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
  }

  build() {
    Column() {
      Button('Load the website that requires the client SSL certificate')
        .onClick(() => {
          this.controller.loadUrl("https://client.badssl.com")
        })
      Web({
        src: "https://www.bing.com/",
        controller: this.controller,
      }).domStorageAccess(true)
        .fileAccess(true)
        .onPageBegin(event => {
          console.info("extensions onpagebegin url " + event.url);
        })
        .onClientAuthenticationRequest((event) => {
          console.info("onClientAuthenticationRequest ");

          this.certManager.grantAppPm().then(result => {
            console.info(`grantAppPm, URI==========${result}`);
            event.handler.confirm(result);
          })
          return true;
        })
        .onSslErrorEventReceive(e => {
          console.info(`onSslErrorEventReceive->${e.error.toString()}`);
        })
        .onErrorReceive((event) => {
          if (event) {
            this.getUIContext().getPromptAction().showToast({
              message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
              alignment: Alignment.Center
            })
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
            console.info('url:' + event.request.getRequestUrl());
          }
        })
        .onTitleReceive(event  => {
          console.info("title received " + event.title);
        })

    }
  }
}
```

## onConfirm

```TypeScript
onConfirm(callback: Callback<OnConfirmEvent, boolean>)
```

Triggered when **confirm()** is invoked by the web page. Call the [handleCancel](arkts-arkweb-jsresult-c.md#handlecancel) or [handleConfirm](arkts-arkweb-jsresult-c.md#handleconfirm) API when this callback is triggered. Otherwise, the render process is blocked.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnConfirmEvent](arkts-arkweb-onconfirmevent-i.md), boolean&gt; | Yes | Callback triggered when **confirm()** is invoked by the web page. Return value: boolean If the callback returns **true**, the application can use the custom dialog box (allows the confirm and cancel operations) and invoke the **JsResult** API to notify the **Web** component the confirmation result. If the callback returns **false**, the processing result of the dialog box is regarded as cancel.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onConfirm((event) => {
          if (event) {
            console.info("event.url:" + event.url);
            console.info("event.message:" + event.message);
            this.uiContext.showAlertDialog({
              title: 'onConfirm',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  event.result.handleCancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            })
          }
          return true;
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
  <h1>WebView onConfirm Demo</h1>
  <button onclick="myFunction()">Click here</button>
  <p id="demo"></p>
  <script>
    function myFunction() {
      let x;
      let r = confirm("click button!");
      if (r == true) {
        x = "ok";
      } else {
        x = "cancel";
      }
      document.getElementById("demo").innerHTML = x;
    }
  </script>
</body>
</html>
```

## onConsole

```TypeScript
onConsole(callback: Callback<OnConsoleEvent, boolean>)
```

Triggered to notify the host application of a JavaScript console message.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnConsoleEvent](arkts-arkweb-onconsoleevent-i.md), boolean&gt; | Yes | Callback used when the web page receives a JavaScript console message. Return value: boolean The value **true** means that the message will not be printed to HiLog logs, and **false** means the opposite.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Button('onconsole message')
        .onClick(() => {
          this.controller.runJavaScript('myFunction()');
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onConsole((event) => {
          if (event) {
            console.info('getMessage:' + event.message.getMessage());
            console.info('getSourceId:' + event.message.getSourceId());
            console.info('getLineNumber:' + event.message.getLineNumber());
            console.info('getMessageLevel:' + event.message.getMessageLevel());
            console.info('getSource:' + event.message.getSource());
          }
          return false;
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<body>
<script>
    function myFunction() {
        console.info("onconsole printf");
    }
</script>
</body>
</html>
```

## onContextMenuHide

```TypeScript
onContextMenuHide(callback: OnContextMenuHideCallback)
```

Triggered when a context menu is hidden after the user clicks the right mouse button or number presses a specific element, such as an image or a link.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnContextMenuHideCallback](arkts-arkweb-oncontextmenuhidecallback-t.md) | Yes | Callback related to menus. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onContextMenuHide(() => {
          console.info("onContextMenuHide callback");
        })
    }
  }
}
```

## onContextMenuShow

```TypeScript
onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean>)
```

Triggered when a context menu is displayed after the user clicks the right mouse button or number presses a specific element, such as an image or a link.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnContextMenuShowEvent](arkts-arkweb-oncontextmenushowevent-i.md), boolean&gt; | Yes | Callback invoked during a call to allow for the display of a custom context menu. Return value: boolean The value **true** means that a custom menu is triggered, and **false** means that the custom menu is ineffective.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { pasteboard } from '@kit.BasicServicesKit';

const TAG = 'ContextMenu';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  private result: WebContextMenuResult | undefined = undefined;
  @State linkUrl: string = '';
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State showMenu: boolean = false;
  uiContext: UIContext = this.getUIContext();

  @Builder
  // Build and trigger a custom menu.
  MenuBuilder() {
    // A component that is used to present a vertical list of items to the user.
    Menu() {
      // A component that is used to represent an item in a menu.
      MenuItem({
        content: 'Cancel',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.undo();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Redo',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.redo();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Paste as plain text',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.pasteAndMatchStyle();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Copy image',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copyImage();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Cut',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.cut();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Copy',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copy();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Paste',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.paste();
          this.showMenu = false;
        })
      MenuItem({
        content: 'Copy link',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          let pasteData = pasteboard.createData('text/plain', this.linkUrl);
          pasteboard.getSystemPasteboard().setData(pasteData, (error) => {
            if (error) {
              return;
            }
          })
          this.showMenu = false;
        })
      MenuItem({
        content: 'Select all',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.selectAll();
          this.showMenu = false;
        })
    }
    .width(150)
    .height(450)
  }

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        // Trigger a custom dialog box.
        .onContextMenuShow((event) => {
          if (event) {
            this.result = event.result
            console.info(TAG + "x coord = " + event.param.x());
            console.info(TAG + "link url = " + event.param.getLinkUrl());
            this.linkUrl = event.param.getLinkUrl();
          }
          console.info(TAG, `x: ${this.offsetX}, y: ${this.offsetY}`);
          this.showMenu = true;
          this.offsetX = 0;
          this.offsetY = Math.max(this.uiContext!.px2vp(event?.param.y() ?? 0) - 0, 0);
          return true;
        })
        .bindPopup(this.showMenu,
          {
            builder: this.MenuBuilder(),
            enableArrow: false,
            placement: Placement.LeftTop,
            offset: { x: this.offsetX, y: this.offsetY },
            mask: false,
            onStateChange: (e) => {
              if (!e.isVisible) {
                this.showMenu = false;
                this.result!.closeContextMenu();
              }
            }
          })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<body>
  <h1>onContextMenuShow</h1>
  <a href="http://www.example.com" style="font-size:27px">URL www.example.com</a>
  <!-- Place any image in the rawfile directory and name it example.png. -->
  <div><img src="example.png"></div>
  <p>Right-click text to display the context menu</p>
</body>
</html>
```

## onControllerAttached

```TypeScript
onControllerAttached(callback: () => void)
```

Triggered when the controller is successfully bound to the **Web** component. The controller must be **WebviewController**. Do not call APIs related to the **Web** component before this callback event. Otherwise, a js-error exception will be thrown.

The web page has not been loaded when the callback is called. Therefore, APIs related to web page operations, such as [zoomIn](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#zoomin), [zoomOut](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#zoomout), cannot be used in the callback. You can use APIs irrelevant to web page operations, such as [loadUrl](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#loadurl), [getWebId](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#getwebid).

For details about the component lifecycle, see [Lifecycle of the Web Component](../../../web/web-event-sequence.md).

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | Callback invoked when the ArkWeb controller is successfully initialized. |

**Examples**

The following example uses loadUrl in the callback to load the web page.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: '', controller: this.controller })
        .onControllerAttached(() => {
          this.controller.loadUrl($rawfile("index.html"));
        })
    }
  }
}
```

The following example uses getWebId in the callback.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onControllerAttached(() => {
          try {
            let id = this.controller.getWebId();
            console.info("id: " + id);
          } catch (error) {
            let code = (error as BusinessError).code;
            let message = (error as BusinessError).message;
            console.error(`ErrorCode: ${code},  Message: ${message}`);
          }
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
    <body>
        <p>Hello World</p>
    </body>
</html>
```

## onDataResubmitted

```TypeScript
onDataResubmitted(callback: Callback<OnDataResubmittedEvent>)
```

Triggered when the web form data can be resubmitted.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnDataResubmittedEvent](arkts-arkweb-ondataresubmittedevent-i.md)&gt; | Yes | Callback invoked when the web form data can be resubmitted.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // After you click Submit on the web page, you can click Refresh to trigger the function again.
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onDataResubmitted((event) => {
          console.info('onDataResubmitted');
          event.handler.resend();
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
 <!DOCTYPE html>
 <html>
 <head>
   <meta charset="utf-8">
 </head>
 <body>
   <form action="http://httpbin.org/post" method="post">
     <input type="text" name="username">
     <input type="submit" name="Submit">
   </form>
 </body>
 </html>
```

## onDetectedBlankScreen

```TypeScript
onDetectedBlankScreen(callback: OnDetectBlankScreenCallback)
```

Called when the **Web** component detects a blank screen.

> **NOTE：**
> 
> - This method must be used with [blankScreenDetectionConfig](#blankscreendetectionconfig).
> Otherwise, the blank screen detection is disabled by default, and the callback is not returned when a blank
> screen is detected.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnDetectBlankScreenCallback](arkts-arkweb-ondetectblankscreencallback-t.md) | Yes | Callback triggered when the **Web** component detects a blank screen. |

**Examples**

```TypeScript
// onDetectedBlankScreen.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .blankScreenDetectionConfig({
          enable: true,
          detectionTiming: [2, 4, 6, 8],
          contentfulNodesCountThreshold: 4,
          detectionMethods:[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN]
        })
        .onDetectedBlankScreen((event: BlankScreenDetectionEventInfo)=>{
          console.info(`Found blank screen on ${event.url}.`);
          console.info(`The blank screen reason is ${event.blankScreenReason}.`);
          console.info(`The blank screen detail is ${event.blankScreenDetails?.detectedContentfulNodesCount}.`);
        })
    }
  }
}
```

## onDownloadStart

```TypeScript
onDownloadStart(callback: Callback<OnDownloadStartEvent>)
```

Triggered to instruct the main application to start downloading a file.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnDownloadStartEvent](arkts-arkweb-ondownloadstartevent-i.md)&gt; | Yes | Callback used when a download starts.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onDownloadStart((event) => {
          if (event) {
            console.info('url:' + event.url)
            console.info('userAgent:' + event.userAgent)
            console.info('contentDisposition:' + event.contentDisposition)
            console.info('contentLength:' + event.contentLength)
            console.info('mimetype:' + event.mimetype)
          }
        })
    }
  }
}
```

## onErrorReceive

```TypeScript
onErrorReceive(callback: Callback<OnErrorReceiveEvent>)
```

Triggered when an error occurs during web page loading. The error may occur on the main resource or sub-resource. You can use [isMainFrame](arkts-arkweb-webresourcerequest-c.md#ismainframe) to determine whether the error occurs on the main resource. For performance reasons, simplify the implementation logic in the callback. This API is called when there is no network connection.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnErrorReceiveEvent](arkts-arkweb-onerrorreceiveevent-i.md)&gt; | Yes | Callback used when an error occurs during web page loading.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onErrorReceive((event) => {
          if (event) {
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
            console.info('url:' + event.request.getRequestUrl());
            console.info('isMainFrame:' + event.request.isMainFrame());
            console.info('isRedirect:' + event.request.isRedirect());
            console.info('isRequestGesture:' + event.request.isRequestGesture());
            console.info('getRequestHeader_headerKey:' + event.request.getRequestHeader().toString());
            let result = event.request.getRequestHeader();
            console.info('The request header result size is ' + result.length);
            for (let i of result) {
              console.info('The request header key is : ' + i.headerKey + ', value is : ' + i.headerValue);
            }
          }
        })
    }
  }
}
```

## onFaviconReceived

```TypeScript
onFaviconReceived(callback: Callback<OnFaviconReceivedEvent>)
```

Triggered when this web page receives a new favicon.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnFaviconReceivedEvent](arkts-arkweb-onfaviconreceivedevent-i.md)&gt; | Yes | Callback invoked when the current web page receives a new favicon.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { image } from '@kit.ImageKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State icon: image.PixelMap | undefined = undefined;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFaviconReceived((event) => {
          console.info('onFaviconReceived');
          this.icon = event.favicon;
        })
    }
  }
}
```

## onFileSelectorShow

```TypeScript
onFileSelectorShow(callback: (event?: { callback: Function, fileSelector: object }) => void)
```

Triggered to process an HTML form whose input type is **file**, in response to the tapping of the **Select File** button.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onShowFileSelector](#onshowfileselector)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (event?: { callback: Function, fileSelector: object }) =&gt; void | Yes | Callback to be executed when the file selector is triggered. |

## onFirstContentfulPaint

```TypeScript
onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent>)
```

Triggered when the first content paint occurs on the web page.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnFirstContentfulPaintEvent](arkts-arkweb-onfirstcontentfulpaintevent-i.md)&gt; | Yes | Callback invoked when the first content paint occurs on the web page.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFirstContentfulPaint(event => {
          if (event) {
            console.info("onFirstContentfulPaint:" + "[navigationStartTick]:" +
            event.navigationStartTick + ", [firstContentfulPaintMs]:" +
            event.firstContentfulPaintMs);
          }
        })
    }
  }
}
```

## onFirstMeaningfulPaint

```TypeScript
onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback)
```

Triggered when the first meaningful paint occurs on the web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFirstMeaningfulPaintCallback](arkts-arkweb-onfirstmeaningfulpaintcallback-t.md) | Yes | Callback invoked when the First Meaningful Paint occurs on the web page. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFirstMeaningfulPaint((details) => {
          console.info("onFirstMeaningfulPaint: [navigationStartTime]= " + details.navigationStartTime +
            ", [firstMeaningfulPaintTime]=" + details.firstMeaningfulPaintTime);
        })
    }
  }
}
```

## onFirstScreenPaint

```TypeScript
onFirstScreenPaint(callback: OnFirstScreenPaintCallback)
```

Triggered when the first screen paint of a web page is complete.

> **NOTE：**
> 
> - First Screen Paint (FSP) records the time taken to render images, texts, and videos in the viewport. It is a
> core performance metric for measuring the duration from a page's initial load to the completion of rendering.
> When no visible elements within the viewport extend beyond the historical rendering area for a certain period of
> time, the moment when the maximum historical rendering of elements in the viewport is achieved is regarded as the
> completion time of first screen paint.
> 
> - After the first screen is drawn, the API waits for a period of time and reports the callback when no new
> rendering information needs to be processed. The callback time is different from the first screen paint
> completion time.
> 
> - If the user performs input operations or scrolls the page while rendering is still in progress, the callback
> function will be reported immediately.
> 
> - This API is used to obtain the first screen rendering time in instant loading scenarios, but it will not
> deliver the expected results if used in preloading or prerendering scenarios.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFirstScreenPaintCallback](arkts-arkweb-onfirstscreenpaintcallback-t.md) | Yes | Callback triggered when the first screen paint of the **Web** component is detected. |

**Examples**

```TypeScript
// onFirstScreenPaint.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFirstScreenPaint((event: FirstScreenPaint)=>{
          console.info(`Found first screen paint on ${event.url}.`);
          console.info(`The navigation start time is ${event.navigationStartTime}.`);
          console.info(`The first screen paint time is ${event.firstScreenPaintTime}.`);
        })
    }
  }
}
```

## onFullScreenEnter

```TypeScript
onFullScreenEnter(callback: OnFullScreenEnterCallback)
```

Triggered when the **Web** component enters full screen mode.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFullScreenEnterCallback](arkts-arkweb-onfullscreenentercallback-t.md) | Yes | Callback invoked when the **Web** component enters full screen mode. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  handler: FullScreenExitHandler | null = null;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFullScreenEnter((event) => {
          console.info("onFullScreenEnter videoWidth: " + event.videoWidth +
            ", videoHeight: " + event.videoHeight);
          // The application can proactively exit fullscreen mode by calling this.handler.exitFullScreen().
          this.handler = event.handler;
        })
    }
  }
}
```

## onFullScreenExit

```TypeScript
onFullScreenExit(callback: () => void)
```

Triggered when the **Web** component exits full screen mode.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | Callback invoked when the component exits full screen mode. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  handler: FullScreenExitHandler | null = null;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFullScreenExit(() => {
          console.info("onFullScreenExit...")
          if (this.handler) {
            this.handler.exitFullScreen();
          }
        })
        .onFullScreenEnter((event) => {
          this.handler = event.handler;
        })
    }
  }
}
```

## onGeolocationHide

```TypeScript
onGeolocationHide(callback: () => void)
```

Triggered to notify the user that the request for obtaining the geolocation information received when [onGeolocationShow](#ongeolocationshow) is called has been canceled.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | Callback invoked when the request for obtaining geolocation information has been canceled. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .geolocationAccess(true)
        .onGeolocationHide(() => {
          console.info("onGeolocationHide...");
        })
    }
  }
}
```

## onGeolocationShow

```TypeScript
onGeolocationShow(callback: Callback<OnGeolocationShowEvent>)
```

Called to notify the user that the geolocation information obtaining request is received. To use this API, the **ohos.permission.LOCATION** and **ohos.permission.APPROXIMATELY_LOCATION** permissions must be configured. This API uses an asynchronous callback to return the result.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnGeolocationShowEvent](arkts-arkweb-ongeolocationshowevent-i.md)&gt; | Yes | Callback triggered when the geolocation permission is requested, returning the geolocation information request object.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, common } from '@kit.AbilityKit';

let atManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  // Component lifecycle function, which is triggered after a component instance is created.
  aboutToAppear(): void {
    let context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    if (!context) {
      console.error("context is undefined");
      return;
    }
    // Request the location permission from the user.
    atManager.requestPermissionsFromUser(context, ["ohos.permission.LOCATION", "ohos.permission.APPROXIMATELY_LOCATION"]).then((data) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    }).catch((error: BusinessError) => {
      console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
    })  
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .geolocationAccess(true)
        .onGeolocationShow((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              confirm: {
                value: 'onConfirm',
                action: () => {
                  // The third parameter of invoke indicates whether to remember the selection status of the current dialog box. If the value is true, the dialog box will not be displayed next time.
                  event.geolocation.invoke(event.origin, true, false);
                }
              },
              cancel: () => {
                // The third parameter of invoke indicates whether to remember the selection status of the current dialog box. If the value is true, the dialog box will not be displayed next time.
                event.geolocation.invoke(event.origin, false, false);
              }
            })
          }
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!DOCTYPE html>
<html>
<body>
<p id="locationInfo">Location information</p>
<button onclick="getLocation()">Obtain Location</button>
<script>
var locationInfo=document.getElementById("locationInfo");
function getLocation(){
  if (navigator.geolocation) {
    // Access to the device location by the frontend page
    navigator.geolocation.getCurrentPosition(showPosition);
  }
}
function showPosition(position){
  locationInfo.innerHTML="Latitude: " + position.coords.latitude + "<br />Longitude: " + position.coords.longitude;
}
</script>
</body>
</html>
```

## onHttpAuthRequest

```TypeScript
onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean>)
```

Triggered when an HTTP authentication request is received.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnHttpAuthRequestEvent](arkts-arkweb-onhttpauthrequestevent-i.md), boolean&gt; | Yes | Callback invoked when the browser requires user credentials. Return value: boolean The value **true** means that the HTTP authentication is successful, and **false** means the opposite.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();
  httpAuth: boolean = false;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onHttpAuthRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'onHttpAuthRequest',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  event.handler.cancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  this.httpAuth = event.handler.isHttpAuthInfoSaved();
                  if (this.httpAuth == false) {
                    webview.WebDataBase.saveHttpAuthCredentials(
                      event.host,
                      event.realm,
                      "2222",
                      "2222"
                    )
                    event.handler.cancel();
                  }
                }
              },
              cancel: () => {
                event.handler.cancel();
              }
            })
          }
          return true;
        })
    }
  }
}
```

## onHttpErrorReceive

```TypeScript
onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent>)
```

Called when an HTTP error (the response code is greater than or equal to 400) occurs during web page resource loading.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnHttpErrorReceiveEvent](arkts-arkweb-onhttperrorreceiveevent-i.md)&gt; | Yes | Callback triggered when an HTTP error occurs during web page resource loading.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onHttpErrorReceive((event) => {
          if (event) {
            console.info('url:' + event.request.getRequestUrl());
            console.info('isMainFrame:' + event.request.isMainFrame());
            console.info('isRedirect:' + event.request.isRedirect());
            console.info('isRequestGesture:' + event.request.isRequestGesture());
            console.info('getResponseData:' + event.response.getResponseData());
            console.info('getResponseEncoding:' + event.response.getResponseEncoding());
            console.info('getResponseMimeType:' + event.response.getResponseMimeType());
            console.info('getResponseCode:' + event.response.getResponseCode());
            console.info('getReasonMessage:' + event.response.getReasonMessage());
            let result = event.request.getRequestHeader();
            console.info('The request header result size is ' + result.length);
            for (let i of result) {
              console.info('The request header key is : ' + i.headerKey + ' , value is : ' + i.headerValue);
            }
            let resph = event.response.getResponseHeader();
            console.info('The response header result size is ' + resph.length);
            for (let i of resph) {
              console.info('The response header key is : ' + i.headerKey + ' , value is : ' + i.headerValue);
            }
          }
        })
    }
  }
}
```

## onInputmethodAttached

```TypeScript
onInputmethodAttached(callback: OnInputmethodAttachedCallback)
```

The callback is triggered when the inputmethod is attached to the IMF.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnInputmethodAttachedCallback](arkts-arkweb-oninputmethodattachedcallback-t.md) | Yes | The triggered callback when the inputmethod is attached to the IMF. |

## onIntelligentTrackingPreventionResult

```TypeScript
onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback)
```

Triggered when the intelligent tracking prevention feature is enabled and the tracker cookie is blocked.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnIntelligentTrackingPreventionCallback](arkts-arkweb-onintelligenttrackingpreventioncallback-t.md) | Yes | Callback invoked when the intelligent tracking prevention feature is enabled and the tracker cookie is blocked. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // The onIntelligentTrackingPreventionResult callback is triggered only when the intelligent tracking prevention feature is enabled.
      Button('enableIntelligentTrackingPrevention')
        .onClick(() => {
          try {
            this.controller.enableIntelligentTrackingPrevention(true);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
        .onIntelligentTrackingPreventionResult((details) => {
          console.info("onIntelligentTrackingPreventionResult: [websiteHost]= " + details.host +
            ", [trackerHost]=" + details.trackerHost);
        })
    }
  }
}
```

## onInterceptKeyboardAttach

```TypeScript
onInterceptKeyboardAttach(callback: WebKeyboardCallback)
```

Triggered before any editable element (such as the **input** tag) on the web page invokes the soft keyboard. The application can use this API to intercept the display of the system's soft keyboard and configure a custom soft keyboard. (With this API, the application can determine whether to use the system's default soft keyboard, a system soft keyboard with a custom Enter key, or a completely application-defined soft keyboard).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [WebKeyboardCallback](arkts-arkweb-webkeyboardcallback-t.md) | Yes | Callback invoked for intercepting the soft keyboard started by the web page. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { inputMethodEngine } from '@kit.IMEKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  webKeyboardController: WebKeyboardController = new WebKeyboardController()
  inputAttributeMap: Map<string, number> = new Map([
      ['UNSPECIFIED', inputMethodEngine.ENTER_KEY_TYPE_UNSPECIFIED],
      ['GO', inputMethodEngine.ENTER_KEY_TYPE_GO],
      ['SEARCH', inputMethodEngine.ENTER_KEY_TYPE_SEARCH],
      ['SEND', inputMethodEngine.ENTER_KEY_TYPE_SEND],
      ['NEXT', inputMethodEngine.ENTER_KEY_TYPE_NEXT],
      ['DONE', inputMethodEngine.ENTER_KEY_TYPE_DONE],
      ['PREVIOUS', inputMethodEngine.ENTER_KEY_TYPE_PREVIOUS]
    ])

    /**
     * Builder for a custom keyboard component.
     */
    @Builder
    customKeyboardBuilder() {
        // Implement a custom keyboard component and connect it to WebKeyboardController to implement operations such as input, deletion, and close.
      Row() {
        Text("Finish")
          .fontSize(20)
          .fontColor(Color.Blue)
          .onClick(() => {
            this.webKeyboardController.close();
          })
        // Insert characters.
        Button("insertText").onClick(() => {
          this.webKeyboardController.insertText('insert ');
        }).margin({
          bottom: 200,
        })
        // Delete characters from the end to the beginning for the length specified by the length parameter.
        Button("deleteForward").onClick(() => {
          this.webKeyboardController.deleteForward(1);
        }).margin({
          bottom: 200,
        })
        // Delete characters from the beginning to the end for the length specified by the length parameter.
        Button("deleteBackward").onClick(() => {
          this.webKeyboardController.deleteBackward(1);
        }).margin({
          left: -220,
        })
        // Insert a function key.
        Button("sendFunctionKey").onClick(() => {
          this.webKeyboardController.sendFunctionKey(6);
        })
      }
    }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
      .onInterceptKeyboardAttach((KeyboardCallbackInfo) => {
        // Initialize option. By default, the default keyboard is used.
        let option: WebKeyboardOptions = {
          useSystemKeyboard: true,
        };
        if (!KeyboardCallbackInfo) {
          return option;
        }

        // Save the WebKeyboardController. When a custom keyboard is used, this handler is required to control behaviors such as input, deletion, and closing of the keyboard.
        this.webKeyboardController = KeyboardCallbackInfo.controller
        let attributes: Record<string, string> = KeyboardCallbackInfo.attributes
        // Traverse attributes.
        let attributeKeys = Object.keys(attributes)
        for (let i = 0; i < attributeKeys.length; i++) {
          console.info('WebCustomKeyboard key = ' + attributeKeys[i] + ', value = ' + attributes[attributeKeys[i]])
        }

        if (attributes) {
          if (attributes['data-keyboard'] == 'customKeyboard') {
            // Determine the soft keyboard to use based on the attributes of editable HTML elements. For example, if the attribute includes data-keyboard and its value is customKeyboard, custom keyboard is used.
            console.info('WebCustomKeyboard use custom keyboard')
            option.useSystemKeyboard = false;
            // Set the custom keyboard builder.
            option.customKeyboard = () => {
              this.customKeyboardBuilder()
            }
            return option;
          }

          if (attributes['keyboard-return'] != undefined) {
            // Determine the soft keyboard to use based on the attributes of editable HTML elements. For example, if the attribute includes keyboard-return, use the system keyboard and specify the type of the system soft keyboard's Enter key.
            option.useSystemKeyboard = true;
            let enterKeyType: number | undefined = this.inputAttributeMap.get(attributes['keyboard-return'])
            if (enterKeyType != undefined) {
              option.enterKeyType = enterKeyType
            }
            return option;
          }
        }

        return option;
      })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
  <!DOCTYPE html>
  <html>

  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0">
  </head>

  <body>

  <p style="font-size:12px">input tag. Original default behavior: </p>
  <input type="text" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as UNSPECIFIED: </p>
  <input type="text" keyboard-return="UNSPECIFIED" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as GO: </p>
  <input type="text" keyboard-return="GO" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as SEARCH: </p>
  <input type="text" keyboard-return="SEARCH" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as SEND: </p>
  <input type="text" keyboard-return="SEND" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as NEXT: </p>
  <input type="text" keyboard-return="NEXT" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as DONE: </p>
  <input type="text" keyboard-return="DONE" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. System keyboard with enterKeyType as PREVIOUS: </p>
  <input type="text" keyboard-return="PREVIOUS" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input tag. Custom keyboard: </p>
  <input type="text" data-keyboard="customKeyboard" style="width: 300px; height: 20px"><br>

  </body>

  </html>
```

## onInterceptKeyEvent

```TypeScript
onInterceptKeyEvent(callback: (event: KeyEvent) => boolean)
```

Triggered when the key event is intercepted and before it is consumed by the webview.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (event: KeyEvent) =&gt; boolean | Yes | Key event that is triggered. The return value is of the Boolean type. The value **true** means to pass the **KeyEvent** to the web kernel, and **false** means the opposite. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onInterceptKeyEvent((event) => {
          if (event.keyCode == 2017 || event.keyCode == 2018) {
            console.info(`onInterceptKeyEvent get event.keyCode ${event.keyCode}`);
            return true;
          }
          return false;
        })
    }
  }
}
```

## onInterceptRequest

```TypeScript
onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse>)
```

Triggered when the **Web** component is about to access a URL. This API is used to block the URL and return the response data. The **onInterceptRequest** API can intercept all redirection requests and return response data, but cannot access POST request body content and obtain buffer data. In this scenario, use [WebSchemeHandler](../arkts-apis/arkts-arkweb-webview-webschemehandler-c.md) based on service requirements.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnInterceptRequestEvent](arkts-arkweb-oninterceptrequestevent-i.md), [WebResourceResponse](arkts-arkweb-webresourceresponse-c.md)&gt; | Yes | Callback invoked when the **Web** component is about to load a URL. The return value is WebResourceResponse. If response data is returned, the data is loaded based on the response data. If no response data is returned, null is returned, indicating that the data is loaded in the original mode.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: WebResourceResponse = new WebResourceResponse();
  heads: Header[] = new Array();
  webData: string = "<!DOCTYPE html>\n" +
    "<html>\n" +
    "<head>\n" +
    "<title>intercept test</title>\n" +
    "</head>\n" +
    "<body>\n" +
    "<h1>intercept test</h1>\n" +
    "</body>\n" +
    "</html>";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onInterceptRequest((event) => {
          if (event) {
            console.info('url:' + event.request.getRequestUrl());
          }
          let head1: Header = {
            headerKey: "Connection",
            headerValue: "keep-alive"
          }
          let head2: Header = {
            headerKey: "Cache-Control",
            headerValue: "no-cache"
          }
          // Add a new element to the end of the array and return the length of the new array.
          let length = this.heads.push(head1);
          length = this.heads.push(head2);
          console.info('The response header result length is :' + length);
          const promise: Promise<String> = new Promise((resolve: Function, reject: Function) => {
            this.responseWeb.setResponseHeader(this.heads);
            this.responseWeb.setResponseData(this.webData);
            this.responseWeb.setResponseEncoding('utf-8');
            this.responseWeb.setResponseMimeType('text/html');
            this.responseWeb.setResponseCode(200);
            this.responseWeb.setReasonMessage('OK');
            resolve("success");
          })
          promise.then(() => {
            console.info("prepare response ready");
            this.responseWeb.setResponseIsReady(true);
          })
          this.responseWeb.setResponseIsReady(false);
          return this.responseWeb;
        })
    }
  }
}
```

## onLargestContentfulPaint

```TypeScript
onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback)
```

Triggered when the largest content paint occurs on the web page.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnLargestContentfulPaintCallback](arkts-arkweb-onlargestcontentfulpaintcallback-t.md) | Yes | Callback invoked when the largest content paint occurs on the web page. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onLargestContentfulPaint((details) => {
          console.info("onLargestContentfulPaint: [navigationStartTime]= " + details.navigationStartTime +
            ", [largestImagePaintTime]=" + details.largestImagePaintTime +
            ", [largestTextPaintTime]=" + details.largestTextPaintTime +
            ", [largestImageLoadStartTime]=" + details.largestImageLoadStartTime +
            ", [largestImageLoadEndTime]=" + details.largestImageLoadEndTime +
            ", [imageBPP]=" + details.imageBPP);
        })
    }
  }
}
```

## onlineImageAccess

```TypeScript
onlineImageAccess(onlineImageAccess: boolean)
```

Sets whether to allow loading of image resources from the network (resources accessed via HTTP and HTTPS). If this attribute is not explicitly called, loading is allowed by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onlineImageAccess | boolean | Yes | Whether to allow loading image resources from the network. The value **true** means that loading is allowed, and **false** means it is not allowed. When **undefined** or **null** is passed in, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onlineImageAccess(true)
    }
  }
}
```

## onLoadFinished

```TypeScript
onLoadFinished(callback: Callback<OnLoadFinishedEvent>)
```

Triggered to notify the host application that the page has been loaded. This method is called only when the main frame loading is complete. For fragment navigations (navigations to **#fragment_id**), **onLoadFinished** is also triggered.

> **NOTE：**
> 
> - Fragment navigation also triggers **onLoadFinished**, but **onPageEnd** is not triggered.
> 
> - If the main frame is automatically redirected before the page is fully loaded, **onLoadFinished** is triggered
> only once. **onPageEnd** is triggered each time the main frame is navigated.
> 
> - When the document of the pop-up window is modified by JavaScript before being loaded, **onLoadStarted** is
> simulated and the URL is set to null, because displaying the URL that is being loaded may be insecure. &lt;b class="
&gt; + topic/ph hi-d/b " id="b145733136532"&gt;onPageBegin&lt;/b
&gt; will not be simulated.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnLoadFinishedEvent](arkts-arkweb-onloadfinishedevent-i.md)&gt; | Yes | Callback triggered when the web page loading is complete. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onLoadFinished((event) => {
          if (event) {
            console.info('url:' + event.url);
          }
        })
    }
  }
}
```

## onLoadIntercept

```TypeScript
onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean>)
```

Triggered when the **Web** component is about to access a URL. This API is used to determine whether to block the access.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnLoadInterceptEvent](arkts-arkweb-onloadinterceptevent-i.md), boolean&gt; | Yes | Callback triggered when a navigation (including iframe navigation) occurs, allowing the application to approve or cancel it. The return value is of the Boolean type. The value **true** means to cancel the navigation, and **false** means the opposite. If **undefined** or **null** is returned, the value is **false**.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onLoadIntercept((event) => {
          console.info('url:' + event.data.getRequestUrl());
          console.info('isMainFrame:' + event.data.isMainFrame());
          console.info('isRedirect:' + event.data.isRedirect());
          console.info('isRequestGesture:' + event.data.isRequestGesture());
          return true;
        })
    }
  }
}
```

## onLoadStarted

```TypeScript
onLoadStarted(callback: Callback<OnLoadStartedEvent>)
```

Triggered to notify the host application that the page loading starts. This method is called once each time the main frame content is loaded. Therefore, for pages that contain iframes or frameset, **onLoadStarted** is called only once for the main frame. This means that when the content of the embedded frame changes, for example, a link or a fragment navigation in the iframe is clicked (navigation to **#fragment_id**), **onLoadStarted** is not invoked.

> **NOTE：**
> 
> - When the document of the pop-up window is modified by JavaScript before being loaded, **onLoadStarted** is
> simulated and the URL is set to null, because displaying the URL that is being loaded may be insecure.
> **onPageBegin** will not be simulated.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnLoadStartedEvent](arkts-arkweb-onloadstartedevent-i.md)&gt; | Yes | Callback triggered when a web page loading starts. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onLoadStarted((event) => {
          if (event) {
            console.info('url:' + event.url);
          }
        })
    }
  }
}
```

## onMicrophoneCaptureStateChange

```TypeScript
onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback)
```

Triggered to notify the user of the microphone state on the current web page, which can be **None**, **Active**, or **Paused**. This API uses an asynchronous callback to return the result.

You can use the **resumeMicrophone**, **pauseMicrophone**, and **stopMicrophone** APIs to resume, pause, and stop the microphone. For details about how to use them, see [resumeMicrophone](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#resumemicrophone).

> **NOTE：**
> 
> **Active** is returned when the current web page is using the microphone; **Paused** is returned when the
> current web page pauses using the microphone; **None** is returned when the current web page does not use the
> microphone.
> 
> When the microphone is being used and the **pauseMicrophone** API is called, the microphone pauses capturing
> audio and **Paused** is returned. You can call the **resumeMicrophone** API using ArkWeb to resume the capture.
> 
> When the microphone is being used and the **stopMicrophone** API is called, the microphone stops capturing audio
> and **None** is returned. Capture cannot be resumed unless the frontend capture is restarted.
> 
> When the microphone is paused and the **resumeMicrophone** API is called, the microphone continues capturing
> audio and **Active** is returned.
> 
> When the microphone is paused and the **stopMicrophone** API is called, the microphone stops capturing audio and
> **None** is returned. Capture cannot be resumed unless the frontend capture is restarted.
> 
> When the microphone is in the **None** state and the **resumeMicrophone** or **pauseMicrophone** API is called,
> the microphone state remains unchanged.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnMicrophoneCaptureStateChangeCallback](arkts-arkweb-onmicrophonecapturestatechangecallback-t.md) | Yes | Callback triggered when the microphone capture state changes. It returns the original and new states. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, PermissionRequestResult, common } from '@kit.AbilityKit';

let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    atManager.requestPermissionsFromUser(context, ['ohos.permission.MICROPHONE'], (err: BusinessError, data: PermissionRequestResult) => {
      console.info('data:' + JSON.stringify(data));
      console.info('data permissions:' + data.permissions);
      console.info('data authResults:' + data.authResults);
    })
  }

  build() {
    Column() {
      Button("resumeMicrophone").onClick(() => {
        try {
          this.controller.resumeMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("pauseMicrophone").onClick(() => {
        try {
          this.controller.pauseMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Button("stopMicrophone").onClick(() => {
        try {
          this.controller.stopMicrophone();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
          }
        })
        .onMicrophoneCaptureStateChange((event: MicrophoneCaptureStateChangeInfo) => {
          console.info("MicrophoneCapture from ", event.originalState, " to ", event.newState);
      })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
 <head>
   <meta charset="UTF-8">
 </head>
 <body>
   <video id="video" width="400px" height="400px" autoplay="autoplay">
   </video>
   <input type="button" title="HTML5 Microphone" value="Enable Microphone" onclick="getMedia()" />
   <script>
     function getMedia() {
       let constraints = {
         video: {
           width: 500,
           height: 500
         },
         audio: true
       }
       let video = document.getElementById("video");
       let promise = navigator.mediaDevices.getUserMedia(constraints);
       promise.then(function(MediaStream) {
         video.srcObject = MediaStream;
         video.play();
       })
     }
   </script>
 </body>
</html>
```

## onNativeEmbedGestureEvent

```TypeScript
onNativeEmbedGestureEvent(callback: (event: NativeEmbedTouchInfo) => void)
```

Triggered when a finger touches a same-layer tag.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (event: NativeEmbedTouchInfo) =&gt; void | Yes | Callback invoked when a finger touches a same-layer tag. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

declare class Params {
  text: string;
  width: number;
  height: number;
}

declare class NodeControllerParams {
  surfaceId: string;
  renderType: NodeRenderType;
  width: number;
  height: number;
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<[Params]> | undefined | null;
  private surfaceId_: string = "";
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: number = 0;
  private height_: number = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
    this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
    return this.rootNode.getFrameNode();
  }

  postEvent(event: TouchEvent | undefined): boolean {
    return this.rootNode?.postTouchEvent(event) as boolean;
  }
}

@Component
struct ButtonComponent {
  @Prop params: Params;
  @State bkColor: Color = Color.Red;

  build() {
    Column() {
      Button(this.params.text)
        .height(50)
        .width(200)
        .border({ width: 2, color: Color.Red })
        .backgroundColor(this.bkColor)

    }
    .width(this.params.width)
    .height(this.params.height)
  }
}

@Builder
function ButtonBuilder(params: Params) {
  ButtonComponent({ params: params })
    .backgroundColor(Color.Green)
}

@Entry
@Component
struct WebComponent {
  @State eventType: string = '';
  controller: webview.WebviewController = new webview.WebviewController();
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: $rawfile("index.html"), controller: this.controller })
          .enableNativeEmbedMode(true)
          .onNativeEmbedLifecycleChange((embed) => {
            if (embed.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: embed.surfaceId as string,
                renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                width: this.uiContext!.px2vp(embed.info?.width),
                height: this.uiContext!.px2vp(embed.info?.height)
              });
              this.nodeController.rebuild();
            }
          })
          .onNativeEmbedGestureEvent((event) => {
            if (event && event.touchEvent) {
              if (event.touchEvent.type == TouchType.Down) {
                this.eventType = 'Down'
              }
              if (event.touchEvent.type == TouchType.Up) {
                this.eventType = 'Up'
              }
              if (event.touchEvent.type == TouchType.Move) {
                this.eventType = 'Move'
              }
              if (event.touchEvent.type == TouchType.Cancel) {
                this.eventType = 'Cancel'
              }
              let ret = this.nodeController.postEvent(event.touchEvent)
              if (event.result) {
                event.result.setGestureEventResult(ret, true);
              }
              console.info("embedId = " + event.embedId);
              console.info("touchType = " + this.eventType);
              console.info("x = " + event.touchEvent.touches[0].x);
              console.info("y = " + event.touchEvent.touches[0].y);
              console.info("Component globalPos:(" + event.touchEvent.target.area.globalPosition.x + "," + event.touchEvent.target.area.globalPosition.y + ")");
              console.info("width = " + event.touchEvent.target.area.width);
              console.info("height = " + event.touchEvent.target.area.height);
            }
          })
      }
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendering Test HTML</title>
    <meta name="viewport">
</head>
<body>
<div>
    <div id="bodyId">
       <embed id="nativeButton" type = "native/button" width="800" height="800" src="test?params1=1" style = "background-color:red"/>
    </div>
</div>
</body>
</html>
```

## onNativeEmbedLifecycleChange

```TypeScript
onNativeEmbedLifecycleChange(callback: (event: NativeEmbedDataInfo) => void)
```

Triggered when the lifecycle of the same-layer tag changes.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (event: NativeEmbedDataInfo) =&gt; void | Yes | Callback invoked when the lifecycle of the same-layer tag changes. |

**Examples**

```TypeScript
// EntryAbility.ets

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    // Added in API version 12: feature to enable the back/forward cache for same-layer rendering.
    let features = new webview.BackForwardCacheSupportedFeatures();
    features.nativeEmbed = true;
    features.mediaTakeOver = true;
    webview.WebviewController.enableBackForwardCache(features);
    webview.WebviewController.initializeWebEngine();
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  @State embedStatus: string = '';
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Default behavior: Click the button to navigate to a new page, close the index page, and destroy the same-layer tag.
      // Added in API version 12: When BFCache is enabled for the page that supports same-layer rendering, clicking the button navigates to a new page, closes the index page, and puts the same-layer tag into BFCache.
      Button('Destroy')
      .onClick(() => {
        try {
          this.controller.loadUrl("www.example.com");
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })

      // Added in API version 12: When BFCache is enabled for the page that supports same-layer rendering, clicking the button to return to the page causes the same-layer tag to exit BFCache.
      Button('backward')
      .onClick(() => {
        try {
          this.controller.backward();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })

      // Added in API version 12: When BFCache is enabled for the page that supports same-layer rendering, clicking a button to advance to the next page causes the same-layer tag to enter BFCache.
      Button('forward')
      .onClick(() => {
        try {
          this.controller.forward();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })


      // Added in API version 12: The web kernel does not allow web pages loaded with non-HTTP and non-HTTPS protocols to enter BFCache.
      // Therefore, to test the ENTER_BFCACHE/LEAVE_BFCACHE states, you need to place the index.html on a web server and load it using the HTTP or HTTPS protocol. Example:
      // Web({ src: "http://xxxx/index.html", controller: this.controller })
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableNativeEmbedMode(true)
        .onNativeEmbedLifecycleChange((event) => {
          // The Create event is triggered when the same-layer tag is detected on the loaded page.
          if (event.status == NativeEmbedStatus.CREATE) {
            this.embedStatus = 'Create';
          }
          // The Update event is triggered when the same-layer tag on the page is moved or scaled.
          if (event.status == NativeEmbedStatus.UPDATE) {
            this.embedStatus = 'Update';
          }
          // The Destroy event is triggered when a user exit the page.
          if (event.status == NativeEmbedStatus.DESTROY) {
            this.embedStatus = 'Destroy';
          }
          // The Enter BFCache event is triggered when the page with the same-layer tag enters BFCache.
          if (event.status == NativeEmbedStatus.ENTER_BFCACHE) {
            this.embedStatus = 'Enter BFCache';
          }
          // The Leave BFCache event is triggered when the page with the same-layer tag leaves BFCache.
          if (event.status == NativeEmbedStatus.LEAVE_BFCACHE) {
            this.embedStatus = 'Leave BFCache';
          }
          console.info("status = " + this.embedStatus);
          console.info("surfaceId = " + event.surfaceId);
          console.info("embedId = " + event.embedId);
          if (event.info) {
            console.info("id = " + event.info.id);
            console.info("type = " + event.info.type);
            console.info("src = " + event.info.src);
            console.info("width = " + event.info.width);
            console.info("height = " + event.info.height);
            console.info("url = " + event.info.url);
          }
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendering Test HTML</title>
    <meta name="viewport">
</head>
<body>
<div>
    <div id="bodyId">
        <embed id="nativeButton" type = "native/button" width="800" height="800" src="test? params1=1" style = "background-color:red"/>
    </div>
</div>
</body>
</html>
```

## onNativeEmbedMouseEvent

```TypeScript
onNativeEmbedMouseEvent(callback: MouseInfoCallback)
```

Triggered when the following operations are performed on the same-layer tag:

- Tapping or holding with the left, middle, or right mouse button.  
- Tapping or holding the left, middle, or right mouse button using the touchpad.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MouseInfoCallback](arkts-arkweb-mouseinfocallback-t.md) | Yes | Callback triggered when a same-layer tag is clicked using the mouse or touchpad. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

declare class Params {
  text: string;
  width: number;
  height: number;
}

declare class NodeControllerParams {
  surfaceId: string;
  renderType: NodeRenderType;
  width: number;
  height: number;
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<[Params]> | undefined | null;
  private surfaceId_: string = "";
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: number = 0;
  private height_: number = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
    this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
    return this.rootNode.getFrameNode();
  }

  postInputEvent(event: TouchEvent | MouseEvent | undefined): boolean {
    return this.rootNode?.postInputEvent(event) as boolean;
  }
}

@Component
struct ButtonComponent {
  @Prop params: Params;
  @State bkColor: Color = Color.Red;

  build() {
    Column() {
      Button(this.params.text)
        .height(50)
        .width(200)
        .border({ width: 2, color: Color.Red })
        .backgroundColor(this.bkColor)

    }
    .width(this.params.width)
    .height(this.params.height)
  }
}

@Builder
function ButtonBuilder(params: Params) {
  ButtonComponent({ params: params })
    .backgroundColor(Color.Green)
}

@Entry
@Component
struct WebComponent {
  @State mouseAction: string = '';
  @State mouseButton: string = '';
  controller: webview.WebviewController = new webview.WebviewController();
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: $rawfile("index.html"), controller: this.controller })
          .enableNativeEmbedMode(true)
          .onNativeEmbedLifecycleChange((embed) => {
            if (embed.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: embed.surfaceId as string,
                renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                width: this.uiContext!.px2vp(embed.info?.width),
                height: this.uiContext!.px2vp(embed.info?.height)
              });
              this.nodeController.rebuild();
            }
          })
          .onNativeEmbedMouseEvent((event) => {
            if (event && event.mouseEvent) {
              let ret = this.nodeController.postInputEvent(event.mouseEvent)
              if (event.result) {
                event.result.setMouseEventResult(ret, true);
              }
            }
          })
      }
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendering Test</title>
    <meta name="viewport">
</head>
<body>
<div>
    <div id="bodyId">
        <embed id="nativeButton" type ="native/button" width="800" height="800" style="background-color:red"/>
    </div>
</div>
</body>
</html>
```

## onNativeEmbedObjectParamChange

```TypeScript
onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback)
```

Called when the **param** element embedded in the same-layer rendering tag **object** changes.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedObjectParamChangeCallback](arkts-arkweb-onnativeembedobjectparamchangecallback-t.md) | Yes | Callback triggered when the **param** element embedded in the same-layer rendering tag **object** is added, modified, or deleted. |

**Examples**

```TypeScript
// xxx.ets
  import { webview } from '@kit.ArkWeb';
  import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from '@kit.ArkUI';

  declare class Params {
    text: string;
    width: number;
    height: number;
  }

  declare class NodeControllerParams {
    surfaceId: string;
    renderType: NodeRenderType;
    width: number;
    height: number;
  }

  class MyNodeController extends NodeController {
    private rootNode: BuilderNode<[Params]> | undefined | null;
    private surfaceId_: string = "";
    private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
    private width_: number = 0;
    private height_: number = 0;

    setRenderOption(params: NodeControllerParams) {
      this.surfaceId_ = params.surfaceId;
      this.renderType_ = params.renderType;
      this.width_ = params.width;
      this.height_ = params.height;
    }

    makeNode(uiContext: UIContext): FrameNode | null {
      this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
      this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
      return this.rootNode.getFrameNode();
    }

    postInputEvent(event: TouchEvent | MouseEvent | undefined): boolean {
      return this.rootNode?.postInputEvent(event) as boolean;
    }
  }

  @Component
  struct ButtonComponent {
    @Prop params: Params;
    @State bkColor: Color = Color.Red;

    build() {
      Column() {
        Button(this.params.text)
          .height(50)
          .width(200)
          .border({ width: 2, color: Color.Red })
          .backgroundColor(this.bkColor)

      }
      .width(this.params.width)
      .height(this.params.height)
    }
  }

  @Builder
  function ButtonBuilder(params: Params) {
    ButtonComponent({ params: params })
      .backgroundColor(Color.Green)
  }

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController();
    private nodeController: MyNodeController = new MyNodeController();
    uiContext: UIContext = this.getUIContext();

    build() {
      Column() {
        Stack() {
          NodeContainer(this.nodeController)
          Web({ src: $rawfile('index.html'), controller: this.controller })
            .enableNativeEmbedMode(true)
            .registerNativeEmbedRule("object", "native")
            .onNativeEmbedLifecycleChange((embed) => {
              if (embed.status == NativeEmbedStatus.CREATE) {
                this.nodeController.setRenderOption({
                  surfaceId: embed.surfaceId as string,
                  renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                  width: this.uiContext!.px2vp(embed.info?.width),
                  height: this.uiContext!.px2vp(embed.info?.height)
                });
                this.nodeController.rebuild();
              }
            })
            .onNativeEmbedObjectParamChange((event) => {
              console.info("embed id: " + event.embedId);
              let paramItems = event.paramItems;
              if (paramItems) {
                for (let i = 0; i < paramItems.length; ++i) {
                  console.info("param info: " + JSON.stringify(paramItems[i]));
                }
              }
            })
        }
      }
    }
  }
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendering Test</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<div>
    <div id="bodyId">
        <object id="nativeButton" type ="native/button" width="300" height="300" style="background-color:red">
          <param id="param-1" name="name-1" value="value1"/>
        </object>
    </div>
</div>
</body>
</html>
```

## onNativeEmbedVisibilityChange

```TypeScript
onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback)
```

Triggered when the visibility of a same-layer tag (such as an **\&lt;embed&gt;** tag or an **\&lt;object&gt;** tag) on a web page changes in the viewport. Same-layer tags are invisible by default. If a tag is visible when the page is loaded for the first time, it is reported. If a tag is invisible, it is not reported. Same-layer tags are considered invisible only when they are all invisible. Partially visible or all visible tags are considered visible. To obtain the visible status change caused by the CSS attributes (including visibility, display, and size change) of the same -layer tag, configure [nativeEmbedOptions](#nativeembedoptions) and set **supportCssDisplayChange** in [EmbedOptions](arkts-arkweb-embedoptions-i.md) to **true**.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedVisibilityChangeCallback](arkts-arkweb-onnativeembedvisibilitychangecallback-t.md) | Yes | Callback invoked when the visibility of a same-layer tag changes. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from "@kit.ArkUI";

declare class Params {
  text: string;
  width: number;
  height: number;
}

declare class NodeControllerParams {
  surfaceId: string;
  renderType: NodeRenderType;
  width: number;
  height: number;
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<[Params]> | undefined | null;
  private surfaceId_: string = "";
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: number = 0;
  private height_: number = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
    this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
    return this.rootNode.getFrameNode();
  }

  postEvent(event: TouchEvent | undefined): boolean {
    return this.rootNode?.postTouchEvent(event) as boolean;
  }
}

@Component
struct ButtonComponent {
  @Prop params: Params;
  @State bkColor: Color = Color.Red;

  build() {
    Column() {
      Button(this.params.text)
        .height(50)
        .width(200)
        .border({ width: 2, color: Color.Red })
        .backgroundColor(this.bkColor)

    }
    .width(this.params.width)
    .height(this.params.height)
  }
}

@Builder
function ButtonBuilder(params: Params) {
  ButtonComponent({ params: params })
    .backgroundColor(Color.Green)
}

@Entry
@Component
struct WebComponent {
  @State embedVisibility: string = '';
  controller: webview.WebviewController = new webview.WebviewController();
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: $rawfile("index.html"), controller: this.controller })
          .enableNativeEmbedMode(true)
          .onNativeEmbedLifecycleChange((embed) => {
            if (embed.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: embed.surfaceId as string,
                renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                width: this.uiContext!.px2vp(embed.info?.width),
                height: this.uiContext!.px2vp(embed.info?.height)
              });
              this.nodeController.rebuild();
            }
          })
          .onNativeEmbedVisibilityChange((embed) => {
            if (embed.visibility) {
              this.embedVisibility = 'Visible';
            } else {
              this.embedVisibility = 'Hidden';
            }
            console.info("embedId = " + embed.embedId);
            console.info("visibility = " + embed.visibility);
          })
      }
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendering Test HTML</title>
    <meta name="viewport">
</head>
<body>
<div>
    <div id="bodyId">
        <embed id="nativeButton" type = "native/button" width="800" height="800" src="test?params1=1" style = "background-color:red"/>
    </div>
</div>
</body>
</html>
```

## onNavigationEntryCommitted

```TypeScript
onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback)
```

Triggered when a web page redirection request is submitted.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNavigationEntryCommittedCallback](arkts-arkweb-onnavigationentrycommittedcallback-t.md) | Yes | Callback invoked when a web page redirection request is submitted. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onNavigationEntryCommitted((details) => {
          console.info("onNavigationEntryCommitted: [isMainFrame]= " + details.isMainFrame +
            ", [isSameDocument]=" + details.isSameDocument +
            ", [didReplaceEntry]=" + details.didReplaceEntry +
            ", [navigationType]=" + details.navigationType +
            ", [url]=" + details.url);
        })
    }
  }
}
```

## onOverrideErrorPage

```TypeScript
onOverrideErrorPage(callback: OnOverrideErrorPageCallback)
```

Triggered when an error occurs during web page loading of main resources. You can use this API to customize the error display page.

> **NOTE：**
> 
> This feature takes effect only after the default error page is enabled by calling the
> [setErrorPageEnabled](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#seterrorpageenabled)
> API.
> 
> If the error code obtained through [errorPageEvent.error.getErrorCode()](arkts-arkweb-webresourceerror-c.md#geterrorcode) is
> greater than 0, it indicates an HTTP error. If the error code is less than 0, it indicates a network error.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnOverrideErrorPageCallback](arkts-arkweb-onoverrideerrorpagecallback-t.md) | Yes | Callback triggered when an error occurs during web page loading. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: "www.error-test.com", controller: this.controller })
       .onControllerAttached(() => {
            this.controller.setErrorPageEnabled(true);
            if (!this.controller.getErrorPageEnabled()) {
                this.controller.setErrorPageEnabled(true);
            }
        })
        .onOverrideErrorPage(event => {
              let htmlStr = "<html><h1>error occur : ";
              htmlStr += event.error.getErrorCode();
              htmlStr += "</h1></html>";
              return htmlStr;
        })
    }
  }
}
```

## onOverrideUrlLoading

```TypeScript
onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback)
```

Triggered when the URL is about to be loaded in the current web page, allowing the host application to obtain control and determine whether to prevent the web page from loading the URL.

> **NOTE：**
> 
> - POST requests do not trigger this callback.
> 
> - This callback is triggered when the iframe loads a non-HTTP(S) document. It is not triggered for HTTP(S)
> documents, **about:blank**, or for any redirection that is started via **loadUrl(url: string)**.
> 
> - Do not call **loadUrl(url: string)** with the same URL in the callback and return **true**. Doing so would
> unnecessarily cancel the current loading and start an identical one. To continue loading the current request URL,
> return **false** instead of calling **loadUrl(url: string)**.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnOverrideUrlLoadingCallback](arkts-arkweb-onoverrideurlloadingcallback-t.md) | Yes | Callback for **onOverrideUrlLoading**. Return value: boolean The value **true** means to stop loading the URL, and the value **false** means the opposite. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onOverrideUrlLoading((webResourceRequest: WebResourceRequest) => {
          if (webResourceRequest && webResourceRequest.getRequestUrl() == "about:blank") {
            return true;
          }
          return false;
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <h1>onOverrideUrlLoading Demo</h1>
  <a href="about:blank">Click here</a>// to visit about:blank.
</body>
</html>
```

## onOverScroll

```TypeScript
onOverScroll(callback: Callback<OnOverScrollEvent>)
```

Triggered when the web page is overscrolled. It is used to notify the application of the overscroll offset.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnOverScrollEvent](arkts-arkweb-onoverscrollevent-i.md)&gt; | Yes | Callback invoked when the web page is overscrolled.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onOverScroll((event) => {
          console.info("x = " + event.xOffset);
          console.info("y = " + event.yOffset);
        })
    }
  }
}
```

## onPageBegin

```TypeScript
onPageBegin(callback: Callback<OnPageBeginEvent>)
```

Triggered when the web page starts to be loaded. This callback is called only for the main frame content, and not for the iframe or frameset content.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnPageBeginEvent](arkts-arkweb-onpagebeginevent-i.md)&gt; | Yes | Callback triggered when a web page loading starts.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageBegin((event) => {
          if (event) {
            console.info('url:' + event.url);
          }
        })
    }
  }
}
```

## onPageEnd

```TypeScript
onPageEnd(callback: Callback<OnPageEndEvent>)
```

Triggered when the web page loading is finished. This callback is called only for the main frame content, and not for the iframe or frameset content.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnPageEndEvent](arkts-arkweb-onpageendevent-i.md)&gt; | Yes | Callback triggered when the web page loading is complete.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageEnd((event) => {
          if (event) {
            console.info('url:' + event.url);
          }
        })
    }
  }
}
```

## onPageVisible

```TypeScript
onPageVisible(callback: Callback<OnPageVisibleEvent>)
```

Triggered when the old page is not displayed and the new page is about to be visible.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnPageVisibleEvent](arkts-arkweb-onpagevisibleevent-i.md)&gt; | Yes | Callback invoked when the old page is not displayed and the new page is about to be visible.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageVisible((event) => {
          console.info('onPageVisible url:' + event.url);
        })
    }
  }
}
```

## onPdfLoadEvent

```TypeScript
onPdfLoadEvent(callback: Callback<OnPdfLoadEvent>)
```

Called to notify the user of whether the PDF page is successfully loaded.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnPdfLoadEvent](arkts-arkweb-onpdfloadevent-i.md)&gt; | Yes | Callback triggered to notify users of whether the PDF page is successfully loaded. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Replace 'https://www.example.com/xxx.pdf' with the actual accessible address.
      Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
        .onPdfLoadEvent((eventInfo: OnPdfLoadEvent) => {
          console.info(`Load event callback called. url: ${eventInfo.url}, result: ${eventInfo.result}.`)
        })
    }
  }
}
```

## onPdfScrollAtBottom

```TypeScript
onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent>)
```

Called to notify the user that the PDF page has been scrolled to the bottom.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnPdfScrollEvent](arkts-arkweb-onpdfscrollevent-i.md)&gt; | Yes | Callback triggered to notify the user that the PDF page has been scrolled to the bottom. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // Replace 'https://www.example.com/xxx.pdf' with the actual accessible address.
      Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
        .onPdfScrollAtBottom((eventInfo: OnPdfScrollEvent) => {
          console.info(`Scroll at bottom callback called. url: ${eventInfo.url}.`)
        })
    }
  }
}
```

## onPermissionRequest

```TypeScript
onPermissionRequest(callback: Callback<OnPermissionRequestEvent>)
```

Triggered when a permission request is received. To call this API, you need to declare the **ohos.permission.CAMERA** and **ohos.permission.MICROPHONE** permissions.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnPermissionRequestEvent](arkts-arkweb-onpermissionrequestevent-i.md)&gt; | Yes | Callback invoked when a permission request is received. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl } from '@kit.AbilityKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  aboutToAppear() {
    // Enable web frontend page debugging.
    webview.WebviewController.setWebDebuggingAccess(true);
    let atManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.uiContext.getHostContext(), ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'])
      .then((data) => {
        console.info('data:' + JSON.stringify(data));
        console.info('data permissions:' + data.permissions);
        console.info('data authResults:' + data.authResults);
      }).catch((error: BusinessError) => {
      console.error(`Failed to request permissions from user. Code is ${error.code}, message is ${error.message}`);
    })
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                event.request.deny();
              }
            })
          }
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
 <!DOCTYPE html>
 <html>
 <head>
   <meta charset="UTF-8">
 </head>
 <body>
 <video id="video" width="500px" height="500px" autoplay></video>
 <canvas id="canvas" width="500px" height="500px"></canvas>
 <br>
 <input type="button" title="HTML5 Camera" value="Enable Camera" onclick="getMedia()"/>
 <script>
   function getMedia()
   {
     let constraints = {
       video: {width: 500, height: 500},
       audio: true
     };
     // Obtain the video camera area.
     let video = document.getElementById("video");
     // Returned Promise object.
     let promise = navigator.mediaDevices.getUserMedia(constraints);
     // then() is asynchronous. Invoke the MediaStream object as a parameter.
     promise.then(function (MediaStream) {
       video.srcObject = MediaStream;
       video.play();
     }).catch(function(error) {
       console.error("Error accessing media devices.", error);
     });
   }
 </script>
 </body>
 </html>
```

## onProgressChange

```TypeScript
onProgressChange(callback: Callback<OnProgressChangeEvent>)
```

Triggered when the web page loading progress changes.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnProgressChangeEvent](arkts-arkweb-onprogresschangeevent-i.md)&gt; | Yes | Callback triggered when the page loading progress changes.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onProgressChange((event) => {
          if (event) {
            console.info('newProgress:' + event.newProgress);
          }
        })
    }
  }
}
```

## onPrompt

```TypeScript
onPrompt(callback: Callback<OnPromptEvent, boolean>)
```

Triggered when **prompt()** is invoked by the web page. Call the [handleCancel](arkts-arkweb-jsresult-c.md#handlecancel) or [handlePromptConfirm](arkts-arkweb-jsresult-c.md#handlepromptconfirm) API when this callback is triggered. Otherwise, the render process is blocked.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnPromptEvent](arkts-arkweb-onpromptevent-i.md), boolean&gt; | Yes | Callback used when **prompt()** is invoked by the web page. Return value: boolean If the callback returns **true**, the application can use the custom dialog box (allows the confirm, cancel, and input operations) and invoke the **JsResult** API to notify the **Web** component the processing result. If the callback returns **false**, the processing result of the dialog box is regarded as cancel.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { CustomContentDialog } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State message: string = 'Hello World';
  @State title: string = 'Hello World';
  @State result: JsResult | null = null;
  promptResult: string = '';
  webviewController: webview.WebviewController = new webview.WebviewController();
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomContentDialog({
      primaryTitle: this.title,
      contentBuilder: () => {
        this.buildContent();
      },
      buttons: [
        {
          value: 'Cancel',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            console.info('Callback when the button is clicked');
            this.result?.handleCancel()
          }
        },
        {
          value: 'OK',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            this.result?.handlePromptConfirm(this.promptResult);
          }
        }
      ],
    }),
    onWillDismiss: () => {
      this.result?.handleCancel();
      this.dialogController.close();
    }
  });

  // Content area of the custom dialog box
  @Builder
  buildContent(): void {
    Column() {
      Text(this.message)
      TextInput()
        .onChange((value) => {
          this.promptResult = value;
        })
        .defaultFocus(true)
    }
    .width('100%')
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.webviewController })
        .onPrompt((event) => {
          if (event) {
            console.info("event.url:" + event.url);
            console.info("event.message:" + event.message);
            console.info("event.value:" + event.value);
            this.title = "Message from" + event.url + "";
            this.message = event.message;
            this.promptResult = event.value;
            this.result = event.result;
            this.dialogController.open();
          }
          return true;
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
  <h1>WebView onPrompt Demo</h1>
  <button onclick="myFunction()">Click here</button>
  <p id="demo"></p>
  <script>
    function myFunction() {
      let message = prompt("Message info", "Hello World");
      if (message != null && message != "") {
        document.getElementById("demo").innerHTML = message;
      }
    }
  </script>
</body>
</html>
```

## onRefreshAccessedHistory

```TypeScript
onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent>)
```

Triggered for the application to update its access history when the navigation is complete.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnRefreshAccessedHistoryEvent](arkts-arkweb-onrefreshaccessedhistoryevent-i.md)&gt; | Yes | Callback triggered when the navigation is complete.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRefreshAccessedHistory((event) => {
          if (event) {
            console.info('url:' + event.url + ' isReload:' + event.isRefreshed);
            console.info('isMainFrame:' + event.isMainFrame);
          }
        })
    }
  }
}
```

## onRenderExited

```TypeScript
onRenderExited(callback: Callback<OnRenderExitedEvent>)
```

Triggered when the rendering process exits abnormally.

A rendering process may be shared by multiple **Web** components. Each affected **Web** component triggers this callback.

You can call the bound **webviewController** APIs to restore the web page when this callback is triggered. For example, [refresh](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#refresh) and [loadUrl](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#loadurl).

For details about the component lifecycle, see [Lifecycle of the Web Components](../../../web/web-event-sequence.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnRenderExitedEvent](arkts-arkweb-onrenderexitedevent-i.md)&gt; | Yes | Callback triggered when the rendering process exits abnormally.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'chrome://crash/', controller: this.controller })
        .onRenderExited((event) => {
          if (event) {
            console.info('reason:' + event.renderExitReason);
          }
        })
    }
  }
}
```

## onRenderExited

```TypeScript
onRenderExited(callback: (event?: { detail: object }) => boolean)
```

Triggered when the rendering process exits due to an error or crash.

A rendering process may be shared by multiple **Web** components. Each affected **Web** component triggers this callback.

You can call the bound **WebViewController** APIs to restore the web page when this callback is triggered. For example, [refresh](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#refresh) and [loadUrl](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#loadurl).

For details, see [Lifecycle of the Web Component](../../../web/web-event-sequence.md).

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onRenderExited](#onrenderexited)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (event?: { detail: object }) =&gt; boolean | Yes | Callback triggered when the rendering process exits abnormally. |

**Examples**

See [onRenderExited](#onrenderexited)

## onRenderProcessNotResponding

```TypeScript
onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback)
```

Triggered when the rendering process does not respond. If the **Web** component cannot process the input event or navigate to a new URL within a proper time range, the web page process is considered unresponsive and the callback is triggered.

If the web page process does not respond, this callback may be triggered until the web page process responds again. In this case, [onRenderProcessResponding](#onrenderprocessresponding) is triggered.

You can terminate the associated rendering process through [terminateRenderProcess](../arkts-apis/arkts-arkweb-webview-webviewcontroller-c.md#terminaterenderprocess), which may affect other **Web** components in the same rendering process.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRenderProcessNotRespondingCallback](arkts-arkweb-onrenderprocessnotrespondingcallback-t.md) | Yes | Callback triggered when the rendering process does not respond. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRenderProcessNotResponding((data) => {
          console.info("onRenderProcessNotResponding: [jsStack]= " + data.jsStack +
            ", [process]=" + data.pid + ", [reason]=" + data.reason);
        })
    }
  }
}
```

## onRenderProcessResponding

```TypeScript
onRenderProcessResponding(callback: OnRenderProcessRespondingCallback)
```

Triggered when the rendering process transitions back to a normal operating state from an unresponsive state. This callback indicates that the web page was not actually frozen.

**Since:** 12

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRenderProcessRespondingCallback](arkts-arkweb-onrenderprocessrespondingcallback-t.md) | Yes | Callback triggered when the rendering process transitions back to a normal operating state from an unresponsive state. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRenderProcessResponding(() => {
          console.info("onRenderProcessResponding again");
        })
    }
  }
}
```

## onRequestSelected

```TypeScript
onRequestSelected(callback: () => void)
```

Triggered when the **Web** component obtains the focus. If the **Web** component loads a web page in the unfocused state and successfully obtains the focus, the callback is triggered twice.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | Callback triggered when a web page obtains the focus. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRequestSelected(() => {
          console.info('onRequestSelected');
        })
    }
  }
}
```

## onResourceLoad

```TypeScript
onResourceLoad(callback: Callback<OnResourceLoadEvent>)
```

Triggered to notify the **Web** component of the URL of the resource file to load.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnResourceLoadEvent](arkts-arkweb-onresourceloadevent-i.md)&gt; | Yes | Callback triggered when a URL is loaded.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onResourceLoad((event) => {
          console.info('onResourceLoad: ' + event.url);
        })
    }
  }
}
```

## onSafeBrowsingCheckFinish

```TypeScript
onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback)
```

Called when the safe browsing check is complete.

**Since:** 21

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-arkweb-onsafebrowsingcheckresultcallback-t.md) | Yes | Callback invoked when the safe browsing check result is received. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSafeBrowsingCheckFinish((callback) => {
          let json: ThreatType = JSON.parse(JSON.stringify(callback)).threatType;
          console.info("onSafeBrowsingCheckFinish: [threatType]= " + json);
        })
    }
  }
}
```

## onSafeBrowsingCheckResult

```TypeScript
onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback)
```

Called when the safe browsing check result is received.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-arkweb-onsafebrowsingcheckresultcallback-t.md) | Yes | Callback invoked when the safe browsing check result is received. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSafeBrowsingCheckResult((callback) => {
          let json: ThreatType = JSON.parse(JSON.stringify(callback)).threatType;
          console.info("onSafeBrowsingCheckResult: [threatType]= " + json);
        })
    }
  }
}
```

## onScaleChange

```TypeScript
onScaleChange(callback: Callback<OnScaleChangeEvent>)
```

Called when the page display scale changes.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnScaleChangeEvent](arkts-arkweb-onscalechangeevent-i.md)&gt; | Yes | Callback triggered when the page display scale changes.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScaleChange((event) => {
          console.info('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
        })
    }
  }
}
```

## onScreenCaptureRequest

```TypeScript
onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent>)
```

Triggered when a screen capture request is received.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnScreenCaptureRequestEvent](arkts-arkweb-onscreencapturerequestevent-i.md)&gt; | Yes | Callback invoked when a screen capture request is received. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScreenCaptureRequest((event) => {
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title: ' + event.handler.getOrigin(),
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.handler.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.handler.grant({ captureMode: WebCaptureMode.HOME_SCREEN });
                }
              },
              cancel: () => {
                event.handler.deny();
              }
            })
          }
        })
    }
  }
}
```

## onScroll

```TypeScript
onScroll(callback: Callback<OnScrollEvent>)
```

Triggered to notify the global scrolling position of the web page.

> **NOTE：**
> 
> The change of the partial scrolling position cannot trigger this callback.
> 
> To determine whether a page is globally scrolled, print **window.pagYOffset** or **window.pagXOffset** before and
> after scrolling.
> 
> If the web page is scrolled globally, the value of **window.pagYOffset** or **window.pagXOffset** changes after
> the web page is scrolled. Otherwise, the value does not change.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnScrollEvent](arkts-arkweb-onscrollevent-i.md)&gt; | Yes | Callback triggered when the page is scrolled to a specified position.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScroll((event) => {
          console.info("x = " + event.xOffset);
          console.info("y = " + event.yOffset);
        })
    }
  }
}
```

## onSearchResultReceive

```TypeScript
onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent>)
```

Triggered to notify the caller of the search result on the web page.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnSearchResultReceiveEvent](arkts-arkweb-onsearchresultreceiveevent-i.md)&gt; | Yes | Callback invoked to notify the caller of the search result on the web page.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSearchResultReceive(ret => {
          if (ret) {
            console.info("on search result receive:" + "[cur]" + ret.activeMatchOrdinal +
              "[total]" + ret.numberOfMatches + "[isDone]" + ret.isDoneCounting);
          }
        })
    }
  }
}
```

## onShowFileSelector

```TypeScript
onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean>)
```

Triggered to process an HTML form whose input type is **file**. If this function is not called or returns **false**, the **Web** component provides the default **Select file** UI. If it returns **true**, the application can customize the response behavior for **Select file**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnShowFileSelectorEvent](arkts-arkweb-onshowfileselectorevent-i.md), boolean&gt; | Yes | Callback triggered to notify the **Web** component of the file selection result. Return value: boolean The value **true** means that you can invoke the system-provided dialog box. The value **false** means that the custom dialog box drawn in the function is ineffective.<br>**Since:** 12 |

**Examples**

Start the file selector.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { picker } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onShowFileSelector((event) => {
          console.info('MyFileUploader onShowFileSelector invoked')
          const documentSelectOptions = new picker.DocumentSelectOptions();
          let uri: string | null = null;
          const documentViewPicker = new picker.DocumentViewPicker();
          documentViewPicker.select(documentSelectOptions).then((documentSelectResult) => {
            uri = documentSelectResult[0];
            console.info('documentViewPicker.select to file succeed and uri is:' + uri);
            if (event) {
              event.result.handleFileList([uri]);
            }
          }).catch((err: BusinessError) => {
            console.error(`Invoke documentViewPicker.select failed, code is ${err.code},  message is ${err.message}`);
          })
          return true;
        })
    }
  }
}
```

Start the photo selector.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { picker } from '@kit.CoreFileKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  async selectFile(result: FileSelectorResult): Promise<void> {
    let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    // Set the mime file type to IMAGE_VIDEO.
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
    // Set the maximum number of media files that can be selected.
    photoSelectOptions.maxSelectNumber = 5;
    let chooseFile: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoSelectOptions);
    // Obtain the list of selected files.
    result.handleFileList(chooseFile.photoUris);
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onShowFileSelector((event) => {
          if (event) {
            this.selectFile(event.result);
          }
          return true;
        })
    }
  }
}
```

Start the camera picker.

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { cameraPicker, camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

async function openCamera(callback: Callback<string>, uiContext: UIContext) {
 let mContext = uiContext.getHostContext() as common.Context;
  try {
    let pickerProfile: cameraPicker.PickerProfile = {
      cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK
    };
    let pickerResult: cameraPicker.PickerResult = await cameraPicker.pick(mContext,
      [cameraPicker.PickerMediaType.PHOTO, cameraPicker.PickerMediaType.VIDEO], pickerProfile);
    callback(pickerResult.resultUri);
  } catch (error) {
    let err = error as BusinessError;
    console.error(`the pick call failed. error code: ${err.code}`);
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onShowFileSelector((event) => {
          openCamera((result) => {
            if (event) {
              console.info('Title is ' + event.fileSelector.getTitle());
              console.info('Mode is ' + event.fileSelector.getMode());
              console.info('Accept types are ' + event.fileSelector.getAcceptType());
              console.info('Capture is ' + event.fileSelector.isCapture());
              console.info('Mime types are ' + event.fileSelector.getMimeTypes());
              event.result.handleFileList([result]);
            }
          }, this.getUIContext())
          return true;
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <form id="upload-form" enctype="multipart/form-data">
    <input type="file" id="upload" name="upload" accept="image/*, video/*"/>
    </form>
</body>
</html>
```

## onSslErrorEvent

```TypeScript
onSslErrorEvent(callback: OnSslErrorEventCallback)
```

Triggered to notify users when an SSL error occurs during the loading of main-frame or subframe resources. To handle SSL errors for loading the main-frame resources, use the [isMainFrame](arkts-arkweb-webresourcerequest-c.md#ismainframe) field to distinguish.

> **NOTE：**
> 
> - Main resource: Entry file for the browser to load web pages, which is usually an HTML document.
> 
> - Subresource: Dependency file referenced by the main resource, which is loaded when a specific tag is
> encountered during main resource parsing.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSslErrorEventCallback](arkts-arkweb-onsslerroreventcallback-t.md) | Yes | Callback invoked when an SSL error occurs during resource loading. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { cert } from '@kit.DeviceCertificateKit';

function LogCertInfo(certChainData : Array<Uint8Array> | undefined) {
  if (!(certChainData instanceof Array)) {
    console.error('failed, cert chain data type is not array');
    return;
  }

  for (let i = 0; i < certChainData.length; i++) {
    let encodeBlobData: cert.EncodingBlob = {
      data: certChainData[i],
      encodingFormat: cert.EncodingFormat.FORMAT_DER
    }
    cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
      if (error) {
        console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
      } else {
        console.info('createX509Cert success');
        console.info(ParseX509CertInfo(x509Cert));
      }
    });
  }
  return;
}

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray[i]);
  }
  return dataString;
}

function ParseX509CertInfo(x509Cert: cert.X509Cert) {
  let res: string = 'getCertificate success, '
    + 'issuer name = '
    + Uint8ArrayToString(x509Cert.getIssuerName().data) + ', subject name = '
    + Uint8ArrayToString(x509Cert.getSubjectName().data) + ', valid start = '
    + x509Cert.getNotBeforeTime()
    + ', valid end = ' + x509Cert.getNotAfterTime();
  return res;
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSslErrorEvent((event: SslErrorEvent) => {
          console.info("onSslErrorEvent url: " + event.url);
          console.info("onSslErrorEvent error: " + event.error);
          console.info("onSslErrorEvent originalUrl: " + event.originalUrl);
          console.info("onSslErrorEvent referrer: " + event.referrer);
          console.info("onSslErrorEvent isFatalError: " + event.isFatalError);
          console.info("onSslErrorEvent isMainFrame: " + event.isMainFrame);
          LogCertInfo(event.certChainData);
          this.uiContext.showAlertDialog({
            title: 'onSslErrorEvent',
            message: 'text',
            primaryButton: {
              value: 'confirm',
              action: () => {
                event.handler.handleConfirm();
              }
            },
            secondaryButton: {
              value: 'cancel',
              action: () => {
                // The value true indicates that the page loading is stopped and the current page is displayed. The value false indicates that the page loading is continued and an error page is displayed.
                event.handler.handleCancel(true);
              }
            },
            cancel: () => {
              event.handler.handleCancel();
            }
          })
        })
    }
  }
}
```

## onSslErrorEventReceive

```TypeScript
onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent>)
```

Triggered to notify the host application when an SSL error occurs while loading the main-frame resource.

To support errors for loading subframe resources, use the [OnSslErrorEvent](#onsslerrorevent) API.

> **NOTE：**
> 
> - Main resource: Entry file for the browser to load web pages, which is usually an HTML document.
> 
> - Subresource: Dependency file referenced by the main resource, which is loaded when a specific tag is
> encountered during main resource parsing.
> 
> - The application needs to call [handler.handleCancel()](arkts-arkweb-sslerrorhandler-c.md#handlecancel) or
> [handler.handleConfirm()](arkts-arkweb-sslerrorhandler-c.md#handleconfirm) to process the callback. Otherwise, resource
> loading is canceled by default. The behavior of **handleConfirm()** or **handleCancel()** may be recorded to
> respond to future SSL errors.
> 
> - The application can display a custom error page or silently record the problem.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnSslErrorEventReceiveEvent](arkts-arkweb-onsslerroreventreceiveevent-i.md)&gt; | Yes | Callback invoked when the web page receives an SSL error.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { cert } from '@kit.DeviceCertificateKit';

function LogCertInfo(certChainData : Array<Uint8Array> | undefined) {
  if (!(certChainData instanceof Array)) {
    console.error('failed, cert chain data type is not array');
    return;
  }

  for (let i = 0; i < certChainData.length; i++) {
    let encodeBlobData: cert.EncodingBlob = {
      data: certChainData[i],
      encodingFormat: cert.EncodingFormat.FORMAT_DER
    }
    cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
      if (error) {
        console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
      } else {
        console.info('createX509Cert success');
        console.info(ParseX509CertInfo(x509Cert));
      }
    });
  }
  return;
}

function Uint8ArrayToString(dataArray: Uint8Array) {
  let dataString = '';
  for (let i = 0; i < dataArray.length; i++) {
    dataString += String.fromCharCode(dataArray[i]);
  }
  return dataString;
}

function ParseX509CertInfo(x509Cert: cert.X509Cert) {
  let res: string = 'getCertificate success, '
    + 'issuer name = '
    + Uint8ArrayToString(x509Cert.getIssuerName().data) + ', subject name = '
    + Uint8ArrayToString(x509Cert.getSubjectName().data) + ', valid start = '
    + x509Cert.getNotBeforeTime()
    + ', valid end = ' + x509Cert.getNotAfterTime();
  return res;
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSslErrorEventReceive((event) => {
          LogCertInfo(event.certChainData);
          this.uiContext.showAlertDialog({
            title: 'onSslErrorEventReceive',
            message: 'text',
            primaryButton: {
              value: 'confirm',
              action: () => {
                event.handler.handleConfirm();
              }
            },
            secondaryButton: {
              value: 'cancel',
              action: () => {
                event.handler.handleCancel();
              }
            },
            cancel: () => {
              event.handler.handleCancel();
            }
          })
        })
    }
  }
}
```

## onSslErrorReceive

```TypeScript
onSslErrorReceive(callback: (event?: { handler: Function, error: object }) => void)
```

Triggered when an SSL error occurs during resource loading.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [onSslErrorEventReceive](#onsslerroreventreceive)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (event?: { handler: Function, error: object }) =&gt; void | Yes | Callback triggered when a web page detects an SSL error. |

## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: TextSelectionChangeCallback)
```

Triggered when the text selection of the **Web** component changes. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> - The gesture selection, mouse selection, and JS selection are supported.
> 
> - This callback is triggered when the selection ends.
> 
> - If the same selection is made using the same method as the previous one, this callback is not triggered. If the
> same selection is made using a different method from the previous one, this callback is triggered.

**Since:** 23

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [TextSelectionChangeCallback](arkts-arkweb-textselectionchangecallback-t.md) | Yes | Callback triggered when the text selection changes. |

**Examples**

```TypeScript
// onTextSelectionChange.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onTextSelectionChange((selectionText: string) => {
          console.info(`Selected text is ${selectionText}.`);
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Example page</title>
</head>
<body>
    Sample text
</body>
</html>
```

## onTitleReceive

```TypeScript
onTitleReceive(callback: Callback<OnTitleReceiveEvent>)
```

Called when the **\&lt;title&gt;** element of the page document changes. If no title is set on the current page, ArkWeb generates a title based on the page URL and returns it to the application before the loading is complete.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnTitleReceiveEvent](arkts-arkweb-ontitlereceiveevent-i.md)&gt; | Yes | Callback triggered when the document title on the page is changed.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onTitleReceive((event) => {
          if (event) {
            console.info('title:' + event.title);
            console.info('isRealTitle:' + event.isRealTitle);
          }
        })
    }
  }
}
```

## onTouchIconUrlReceived

```TypeScript
onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent>)
```

Triggered when an apple-touch-icon URL is received.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnTouchIconUrlReceivedEvent](arkts-arkweb-ontouchiconurlreceivedevent-i.md)&gt; | Yes | Callback invoked when an apple-touch-icon URL is received.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.baidu.com', controller: this.controller })
        .onTouchIconUrlReceived((event) => {
          console.info('onTouchIconUrlReceived:' + JSON.stringify(event));
        })
    }
  }
}
```

## onUrlLoadIntercept

```TypeScript
onUrlLoadIntercept(callback: (event?: { data: string | WebResourceRequest }) => boolean)
```

Triggered when the **Web** component is about to access a URL. This API is used to determine whether to block the access.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** onLoadIntercept

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (event?: { data: string \| WebResourceRequest }) =&gt; boolean | Yes | URL information. The return value is of the Boolean type. If **true** is returned, the access is blocked. Otherwise, the access is allowed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onUrlLoadIntercept((event) => {
          if (event) {
            console.info('onUrlLoadIntercept ' + event.data.toString());
          }
          return true
        })
    }
  }
}
```

## onVerifyPin

```TypeScript
onVerifyPin(callback: OnVerifyPinCallback)
```

Triggered to notify the user of PIN verification. This API uses an asynchronous callback to return the result.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnVerifyPinCallback](arkts-arkweb-onverifypincallback-t.md) | Yes | Callback triggered to notify the user of PIN authentication. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: WebviewController = new webview.WebviewController();
  uiContext : UIContext = this.getUIContext();
  context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
  }

  build() {
    Column() {
      Button('Load the website that requires the client SSL certificate')
        .onClick(() => {
          this.controller.loadUrl("https://client.badssl.com")
        })
      Web({
        src: "https://www.bing.com/",
        controller: this.controller,
      }).domStorageAccess(true)
        .fileAccess(true)
        .onPageBegin(event => {
          console.info("extensions onpagebegin url " + event.url);
        })
        .onClientAuthenticationRequest((event) => {
          // Receive the client certificate request event.
          console.info(`onClientAuthenticationRequest`);
          try {
            let certTypes: Array<certificateManagerDialog.CertificateType> = [
              certificateManagerDialog.CertificateType.CREDENTIAL_UKEY
            ];
            // Invoke the certificate management to open the certificate selection dialog box.
            certificateManagerDialog.openAuthorizeDialog(this.context, { certTypes: certTypes })
              .then((data: certificateManagerDialog.CertReference) => {
                console.info(`openAuthorizeDialog request cred auth success`)
                // Notify the web page that the UKey certificate is selected.
                event.handler.confirm(data.keyUri, CredentialType.CREDENTIAL_UKEY);
              }).catch((err: BusinessError) => {
              console.error(`openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(err)}`);
            })
          } catch (e) {
            console.error(`openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(e)}`);
          }
          return true;
        })
        .onVerifyPin((event) => {
          // Receive the PIN verification request event.
          console.info(`onVerifyPin`);
          // Invoke the certificate management to open the PIN input box.
          certificateManagerDialog.openUkeyAuthDialog(this.context, {keyUri: event.identity})
            .then(() => {
              // Notify the web page that the PIN verification is successful.
              console.info(`onVerifyPin success`);
              event.handler.confirm(PinVerifyResult.PIN_VERIFICATION_SUCCESS);
            }).catch((err: BusinessError) => {
            // Notify the web page that the PIN verification fails.
            console.info(`onVerifyPin fail`);
            event.handler.confirm(PinVerifyResult.PIN_VERIFICATION_FAILED);
          })
        })
        .onSslErrorEventReceive(e => {
          console.info(`onSslErrorEventReceive->${e.error.toString()}`);
        })
        .onErrorReceive((event) => {
          if (event) {
            this.getUIContext().getPromptAction().showToast({
              message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
              alignment: Alignment.Center
            })
            console.info('getErrorInfo:' + event.error.getErrorInfo());
            console.info('getErrorCode:' + event.error.getErrorCode());
            console.info('url:' + event.request.getRequestUrl());
          }
        })
        .onTitleReceive(event  => {
          console.info("title received " + event.title);
        })

    }
  }
}
```

## onViewportFitChanged

```TypeScript
onViewportFitChanged(callback: OnViewportFitChangedCallback)
```

Triggered when the **viewport-fit** configuration in the web page's **meta** tag changes. The application can adapt its layout to the viewport within this callback.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnViewportFitChangedCallback](arkts-arkweb-onviewportfitchangedcallback-t.md) | Yes | Callback invoked when the **viewport-fit** configuration in the web page's **meta** tag changes. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onViewportFitChanged((data) => {
          let jsonData = JSON.stringify(data);
          let viewportFit: ViewportFit = JSON.parse(jsonData).viewportFit;
          if (viewportFit === ViewportFit.COVER) {
            // The index.html web page supports immersive layout. You can call expandSafeArea to adjust the Web component layout viewport to cover the safe area (status bar or navigation bar).
          } else if (viewportFit === ViewportFit.CONTAINS) {
            // The index.html web page does not support immersive layout. You can call expandSafeArea to adjust the Web component layout viewport as a safe area.
          } else {
            // Default value. No processing is required.
          }
        })
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width,viewport-fit=cover">
  </head>
  <body>
    <div style="position: absolute; bottom: 0; margin-bottom: env(safe-area-inset-bottom)"></div>
  </body>
</html>
```

## onWindowExit

```TypeScript
onWindowExit(callback: () => void)
```

Triggered when this window is closed. This API works in the same way as [onWindowNew](#onwindownew). For security, applications should notify users that the pages they interact with are closed.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | () =&gt; void | Yes | Callback invoked when the window is closed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onWindowExit(() => {
          console.info("onWindowExit...");
        })
    }
  }
}
```

## onWindowNew

```TypeScript
onWindowNew(callback: Callback<OnWindowNewEvent>)
```

Triggered to notify the user of a new window creation request, when **multiWindowAccess** is enabled.

If the [setWebController](arkts-arkweb-controllerhandler-c.md#setwebcontroller) API is not called, the render process will be blocked.

If no new window is created, set this parameter to **null** when invoking the [setWebController](arkts-arkweb-controllerhandler-c.md#setwebcontroller) API to notify the **Web** component that no new window is created.

The new window cannot be directly overlaid on the original **Web** component, and its URL (for example, address bar) must be clearly displayed in the same way as the main page to prevent confusion. If visible management of trusted URLs cannot be implemented, consider prohibiting the creation of new windows.

Note that the source of a new window request cannot be reliably traced. The request may be initiated by a third- party iframe. By default, the application needs to take defense measures such as sandbox isolation and permission restriction to ensure security.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnWindowNewEvent](arkts-arkweb-onwindownewevent-i.md)&gt; | Yes | Callback invoked when the web page requests the user to create a window.<br>**Since:** 12 |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

// There are two Web components on the same page. When the WebComponent object opens a new window, the NewWebViewComp object is displayed.
@CustomDialog
struct NewWebViewComp {
  controller?: CustomDialogController;
  webviewController1: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: "www.example.com", controller: this.webviewController1 })
        .javaScriptAccess(true)
        .multiWindowAccess(false)
        .onWindowExit(() => {
          console.info("NewWebViewComp onWindowExit");
          if (this.controller) {
            this.controller.close();
          }
        })
    }
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  dialogController: CustomDialogController | null = null;

  build() {
    Column() {
      Web({ src: $rawfile("window.html"), controller: this.controller })
        .javaScriptAccess(true)
        // MultiWindowAccess needs to be enabled.
        .multiWindowAccess(true)
        .allowWindowOpenMethod(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController.close();
          }
          let popController: webview.WebviewController = new webview.WebviewController();
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController })
          })
          this.dialogController.open();
          // Return the WebviewController object corresponding to the new window to the web kernel.
          // If the event.handler.setWebController API is not called, the render process will be blocked.
          // If no new window is created, set the value of event.handler.setWebController to null to notify the Web component that no new window is created.
          event.handler.setWebController(popController);
        })
    }
  }
}
```

```TypeScript
<!-- Code of the window.html page -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<a href="#" onclick="openNewWindow('https://www.example.com')">Open a new page</a>
<script type="text/javascript">
    function openNewWindow(url) {
      window.open(url, 'example');
      return false;
    }
</script>
</body>
</html>
```

## onWindowNewExt

```TypeScript
onWindowNewExt(callback: Callback<OnWindowNewExtEvent>)
```

Triggered to notify the user of a new window creation request when [multiWindowAccess](#multiwindowaccess) is enabled.

> **NOTE：**
> 
> - If the [setWebController](arkts-arkweb-controllerhandler-c.md#setwebcontroller) API is not called, the render process will
> be blocked.
> 
> - If no new window is created, the [setWebController](arkts-arkweb-controllerhandler-c.md#setwebcontroller) API is called and
> set to **null**, notifying the web page that no new window is created.
> 
> - The new window cannot be directly overlaid on the original **Web** component, and its URL (for example, address
> bar) must be clearly displayed in the same way as the main page to prevent confusion. If the URL display and
> verification mechanism cannot be ensured to be reliable, you need to disable the creation of new windows.
> 
> - The source of a new window request cannot be reliably traced. The request may be initiated by a third-party
> iframe. By default, the application needs to take defense measures such as sandbox isolation and permission
> restriction to ensure security.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | Callback&lt;[OnWindowNewExtEvent](arkts-arkweb-onwindownewextevent-i.md)&gt; | Yes | Callback invoked when the web page requests the user to create a window. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

// There are two Web components on the same page. When the WebComponent object opens a new window, the NewWebViewComp object is displayed.
@CustomDialog
struct NewWebViewComp {
controller?: CustomDialogController;
webviewController1: webview.WebviewController = new webview.WebviewController();

build() {
  Column() {
    Web({ src: "www.example.com", controller: this.webviewController1 })
      .javaScriptAccess(true)
      .multiWindowAccess(false)
      .onWindowExit(() => {
        console.info("NewWebViewComp onWindowExit");
        if (this.controller) {
          this.controller.close();
        }
      })
    }
  }
}

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController();
dialogController: CustomDialogController | null = null;

build() {
  Column() {
    Web({ src: $rawfile("window.html"), controller: this.controller })
      .javaScriptAccess(true)
      // Enable multiWindowAccess.
      .multiWindowAccess(true)
      .allowWindowOpenMethod(true)
      .onWindowNewExt((event) => {
        // Open a new window using the event.navigationPolicy request.
        console.info("navigationAction: ", event.navigationPolicy)
        // Create a new window based on the size and position information in event.windowFeatures.
        console.info("windowFeatures: ", JSON.stringify(event.windowFeatures))
        if (this.dialogController) {
          this.dialogController.close();
        }
        let popController: webview.WebviewController = new webview.WebviewController();
        this.dialogController = new CustomDialogController({
          builder: NewWebViewComp({ webviewController1: popController })
        })
        this.dialogController.open();
        // Return the WebviewController object corresponding to the new window to the web kernel.
        // If the event.handler.setWebController API is not called, the render process will be blocked.
        // If no new window is created, set the value of event.handler.setWebController to null to notify the Web component that no new window is created.
        event.handler.setWebController(popController);
      })
    }
  }
}
```

```TypeScript
<!-- Code of the window.html page -->
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
  <a href="#" onclick="openNewWindow('https://www.example.com')">Open a new page</a>
  <script type="text/javascript">
      function openNewWindow(url) {
        window.open(url, 'example', 'left=60,top=80,width=800,height=600');
        return false;
      }
  </script>
  </body>
  </html>
```

## optimizeParserBudget

```TypeScript
optimizeParserBudget(optimizeParserBudget: boolean)
```

Sets whether to enable segment-based HTML parsing optimization. If no attribute is explicitly called, the parsing time is used as the segment point by default.

To avoid occupying too many main thread resources and enable progressive loading of web pages, the ArkWeb kernel uses the segment-based parsing policy when parsing the HTML files. By default, the ArkWeb kernel uses the parsing time as the segment point. When the parsing time exceeds the threshold, the parsing is interrupted and then the layout and rendering operations are performed.

After optimization is enabled, the ArkWeb kernel not only checks whether the parsing time exceeds the limit, but also additionally determines whether the number of parsed tokens (the smallest parsing units of an HTML document, such as `&lt;div&gt;`, `attr="xxx"`, etc.) exceeds the threshold specified by the kernel, and lowers this threshold. When the FCP (First Contentful Paint) of the page is triggered, the default interrupt judgment logic is restored. This makes the parsing operations before FCP more frequent, thereby increasing the possibility that the first-frame content is parsed and enters the rendering phase earlier, while effectively reducing the rendering workload of the first frame, ultimately advancing the FCP time.

When the FCP of a page is triggered, the default segment parsing logic is restored. Therefore, the segment-based HTML parsing optimization takes effect only for the first page loaded by each **Web** component.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| optimizeParserBudget | boolean | Yes | Whether to enable segment-based HTML parsing optimization. The value **true** means to use the number of parsed records instead of the parsing time as the segment point for HTML segment parsing, and reduce the upper limit of the number of parsed records in each segment. The value **false** means to use the parsing time as the segment point for HTML segment parsing. If **undefined** or **null** is passed in, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController()
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .optimizeParserBudget(true)
    }
  }
}
```

## overScrollMode

```TypeScript
overScrollMode(mode: OverScrollMode)
```

Sets the over-scroll mode of the **Web** component. When enabled, if the user scrolls to the edge of the root web page, the **Web** component bounces back with an elastic animation, and inner pages on the root page do not trigger the bounce effect. If this attribute is not explicitly called, the over-scroll mode is disabled by default.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [OverScrollMode](arkts-arkweb-overscrollmode-e.md) | Yes | Whether to enable the overscroll mode. When **undefined** or **null** is passed in, the value is **OverScrollMode.NEVER**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State mode: OverScrollMode = OverScrollMode.ALWAYS;
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .overScrollMode(this.mode)
    }
  }
}
```

## overviewModeAccess

```TypeScript
overviewModeAccess(overviewModeAccess: boolean)
```

Sets whether to load web pages by using the overview mode. That is, zoom out the content to fit the screen width. When this attribute is not explicitly called, web pages can be loaded in overview mode by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| overviewModeAccess | boolean | Yes | Whether to load web pages in overview mode. The value **true** means to use overview mode, and **false** means not to use it. The default value is **false** when undefined or null is passed in. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .overviewModeAccess(true)
    }
  }
}
```

## password

```TypeScript
password(password: boolean)
```

Sets whether to save the password. This API is an empty API.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** enableAutofill

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| password | boolean | Yes | Whether to allow the web component to save passwords. The value **true** means the web component is allowed to save passwords, and **false** means the opposite. If **undefined** or **null** is passed, the default value **false** is used. |

## pinchSmooth

```TypeScript
pinchSmooth(isEnabled: boolean)
```

Sets whether to enable pinch smooth mode for the web page. When this attribute is not explicitly called, pinch smooth mode is disabled by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean | Yes | Whether to enable pinch smooth mode for the web page. The value **true** means to enable pinch smooth mode, and **false** means the opposite. If **undefined** or **null** is passed in, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .pinchSmooth(true)
    }
  }
}
```

## registerNativeEmbedRule

```TypeScript
registerNativeEmbedRule(tag: string, type:string)
```

Registers the HTML tag name and type for same-layer rendering. The tag name only supports &lt;object\&gt; and &lt;embed\&gt;. The tag type only supports visible ASCII characters.

If the specified type is the same as the W3C standard &lt;object\&gt; or &lt;embed\&gt; type, the ArkWeb kernel identifies the type as a non-same-layer tag.

This API is also controlled by **enableNativeEmbedMode** and does not take effect when same-layer rendering is disabled. When this API is not used, the ArkWeb kernel recognizes the &lt;embed\&gt; tags with the "native/" prefix as same-layer tags.

For details, see [Using Same-Layer Rendering](../../../web/web-same-layer.md#rendering-text-boxes-at-the-same-layer-on-web-pages).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string | Yes | Tag name. |
| type | string | Yes | Tag type. The ArkWeb kernel uses a prefix to match this parameter. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { NodeController, BuilderNode, NodeRenderType, FrameNode, UIContext } from '@kit.ArkUI';

declare class Params {
  text: string;
  width: number;
  height: number;
}

declare class NodeControllerParams {
  surfaceId: string;
  renderType: NodeRenderType;
  width: number;
  height: number;
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<[Params]> | undefined | null;
  private surfaceId_: string = "";
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: number = 0;
  private height_: number = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
    this.rootNode.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
    return this.rootNode.getFrameNode();
  }

  postInputEvent(event: TouchEvent | MouseEvent | undefined): boolean {
    return this.rootNode?.postInputEvent(event) as boolean;
  }
}

@Component
struct ButtonComponent {
  @Prop params: Params;
  @State bkColor: Color = Color.Red;

  build() {
    Column() {
      Button(this.params.text)
        .height(50)
        .width(200)
        .border({ width: 2, color: Color.Red })
        .backgroundColor(this.bkColor)
    }
    .width(this.params.width)
    .height(this.params.height)
  }
}

@Builder
function ButtonBuilder(params: Params) {
  ButtonComponent({ params: params })
    .backgroundColor(Color.Green)
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: $rawfile('index.html'), controller: this.controller })
           // Enable same-layer rendering.
          .enableNativeEmbedMode(true)
           // Register the same-layer tag of <object> and type of "native."
          .registerNativeEmbedRule("object", "native")
           // Obtain the lifecycle change data of the <object> tag.
          .onNativeEmbedLifecycleChange((object) => {
            if (object.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: object.surfaceId as string,
                renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                width: this.uiContext!.px2vp(object.info?.width),
                height: this.uiContext!.px2vp(object.info?.height)
              });
              this.nodeController.rebuild();
            }
          })
      }
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>Same-Layer Rendering Test</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<div>
    <div id="bodyId">
        <object id="nativeButton" type ="native/button" width="300" height="300" style="background-color:red">
        </object>
    </div>
</div>
</body>
</html>
```

## rotateRenderEffect

```TypeScript
rotateRenderEffect(effect: WebRotateEffect)
```

Sets how the final state of the **Web** component's content is rendered during its width and height animation process when the component rotates. If this attribute is not explicitly called, by default, the component's content stays at the final size and always aligned with the upper left corner of the component.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | [WebRotateEffect](arkts-arkweb-webrotateeffect-e.md) | Yes | How the final state of the **Web** component's content is rendered during its width and height animation process when the component rotates. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State effect: WebRotateEffect = WebRotateEffect.TOPLEFT_EFFECT;
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .rotateRenderEffect(this.effect)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <p>Test Web Page</p>
</body>
</html>
```

## runJavaScriptOnDocumentEnd

```TypeScript
runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the specified page or document has been loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**
> 
> - The script runs after any JavaScript code on the page, and the DOM tree has already been loaded and rendered at
> that point.
> 
> - The scripts are executed in the order of the array.
> 
> - When scripts with identical content are injected multiple times, they are silently deduplicated without display
> or notification, and the **scriptRules** from the first injection are used.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes | Script item array to be injected. When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  private jsStr: string =
    "window.document.getElementById(\"result\").innerHTML = 'this is msg from runJavaScriptOnDocumentEnd'";
  private jsStr2: string = "console.info('runJavaScriptOnDocumentEnd urlRegexRules Matching succeeded.')";
  @State scripts: Array<ScriptItem> = [
    { script: this.jsStr, scriptRules: ["*"] },
    { script: this.jsStr2, scriptRules: [], urlRegexRules: [{secondLevelDomain: "", rule: ".*index.html"}] }
  ];

  build() {
    Column({ space: 20 }) {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .backgroundColor(Color.Grey)
        .runJavaScriptOnDocumentEnd(this.scripts)
        .width('100%')
        .height('100%')
    }
  }
}
```

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;">
Hello world!
<div id="result">test msg</div>
</body>
</html>
```

## runJavaScriptOnDocumentStart

```TypeScript
runJavaScriptOnDocumentStart(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the specified page or document starts to be loaded, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**
> 
> - The script is injected after the root element (HTML Element) of the web document is created but before any
> other content is loaded.
> 
> - The scripts are executed in the order of the array.
> 
> - When scripts with identical content are injected multiple times, they are silently deduplicated without display
> or notification, and the **scriptRules** from the first injection are used.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes | Script item array to be injected. When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components. |

## runJavaScriptOnHeadEnd

```TypeScript
runJavaScriptOnHeadEnd(scripts: Array<ScriptItem>)
```

Injects a JavaScript script into the **Web** component. When the **head** tag of the DOM tree is parsed, the script is executed on any page whose source matches **scriptRules**. When this attribute is not explicitly called, JavaScript scripts are not injected into the **Web** component by default.

> **NOTE：**
> 
> - This script is executed in the array order.
> 
> - If a script with the same content is injected for multiple times, the script is silently deduplicated, not
> displayed, and no notification is displayed. The **scriptRules** of the first injection is used.

**Since:** 15

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-scriptitem-i.md)&gt; | Yes | Script item array to be injected. When **undefined** or **null** is passed in, JavaScript scripts are not injected into **Web** components. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  private jsStr: string =
    "window.document.getElementById(\"result\").innerHTML = 'this is msg from runJavaScriptOnHeadEnd'";
  private jsStr2: string = "console.info('runJavaScriptOnHeadEnd urlRegexRules Matching succeeded.')";
  @State scripts: Array<ScriptItem> = [
    { script: this.jsStr, scriptRules: ["*"] },
    { script: this.jsStr2, scriptRules: [], urlRegexRules: [{secondLevelDomain: "", rule: ".*index.html"}] }
  ];

  build() {
    Column({ space: 20 }) {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .javaScriptAccess(true)
        .domStorageAccess(true)
        .backgroundColor(Color.Grey)
        .runJavaScriptOnHeadEnd(this.scripts)
        .width('100%')
        .height('100%')
    }
  }
}
```

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body style="font-size: 30px;">
Hello world!
<div id="result">test msg</div>
</body>
</html>
```

## scrollbarLayoutPolicy

```TypeScript
scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy)
```

Selects the layout mode of the vertical scrollbar within the **Web** component, used to adapt to the writing direction of different languages. The **CONTENT** mode is suitable for scenarios where the web page CSS **direction** attribute needs to be followed, while the **SYSTEM** mode is suitable for scenarios in multilingual apps where the system language direction needs to be followed, such as for right-to-left languages like Arabic and Hebrew.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [ScrollbarLayoutPolicy](arkts-arkweb-scrollbarlayoutpolicy-e.md) | Yes | Sets the layout mode of the vertical scrollbar within the **Web** component. Options: **CONTENT** (follows the web page CSS **direction** attribute), **SYSTEM** (lays out according to the left-to-right or right-to-left writing direction of the system language. For right-to-left languages, the scrollbar is laid out on the left side. This applies to all nested scrollbars within the web page). |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .width('100%')
        .height('100%')
        // Set to SYSTEM to follow the system language direction layout. Set to CONTENT to use the Web style layout.
        .scrollbarLayoutPolicy(ScrollbarLayoutPolicy.SYSTEM)
    }
  }
}
```

## selectionMenuOptions

```TypeScript
selectionMenuOptions(expandedMenuOptions: Array<ExpandedMenuItemOptions>)
```

Sets the extended options of the custom context menu on selection, including the text content, icon, and callback.

The API only supports the selection of plain text; if the selected content contains images or other non-text elements, the **action** information may display garbled content.

> **NOTE：**
> 
> When used together with [editMenuOptions](#editmenuoptions), this API does not take effect.

**Since:** 12

**Deprecated since:** 20

**Substitutes:** editMenuOptions

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| expandedMenuOptions | Array&lt;[ExpandedMenuItemOptions](arkts-arkweb-expandedmenuitemoptions-i.md)&gt; | Yes | Extended options of the custom context menu on selection. The number of menu options, menu content size, and start icon size must be the same as those of the ArkUI Menu component. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State menuOptionArray: Array<ExpandedMenuItemOptions> = [
    {content: 'Apple', startIcon: $r('app.media.icon'), action: (selectedText) => {
      console.info('select info ' + selectedText.toString());
    }},
    {content: 'Banana', startIcon: $r('app.media.icon'), action: (selectedText) => {
      console.info('select info ' + selectedText.toString());
    }}
  ];

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
      .selectionMenuOptions(this.menuOptionArray)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>Test Web Page</title>
</head>
<body>
  <h1>selectionMenuOptions Demo</h1>
  <span>selection menu options</span>
</body>
</html>
```

## tableData

```TypeScript
tableData(tableData: boolean)
```

Sets whether to save form data. When this attribute is not explicitly called, the **Web** component is allowed to save form data by default. This API is an empty API.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** enableAutofill

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tableData | boolean | Yes | Whether to allow the Web component to save form data. The value **true** means the Web component is allowed to save form data, and **false** means the opposite. If **undefined** or **null** is passed, the value is **true**. |

## textAutosizing

```TypeScript
textAutosizing(textAutosizing: boolean)
```

Sets whether to enable automatic font sizing for the **Web** component. When no attribute is explicitly called, automatic font sizing is enabled for the **Web** component by default.

After automatic font sizing takes effect, any text smaller than 16 px is enlarged to fall between 16 px and 32 px. This eliminates readability issues on narrow screens (viewport &lt; 980 px) where mobile-specific layouts are absent.

&gt; **NOTE：**
> 
> - The preconditions for automatic font sizing to take effect are as follows:
> 
> - The device type should be phone, tablet, wearable, or TV.
> 
> - The viewport width of the **Web** component is less than 980 px.
> 
> - The page is text-heavy: font size (px) × character count ≥ 3920.
> 
> - **metaViewport** is not set on the frontend, or the **metaViewport** does not contain the **width** and
> **initial-scale** attributes.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textAutosizing | boolean | Yes | Whether to enable automatic text resizing. The value **true** means to enable automatic text resizing, and **false** means the opposite. When **undefined** or **null** is passed in, the value is **true**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .textAutosizing(false)
    }
  }
}
```

## textZoomAtio

```TypeScript
textZoomAtio(textZoomAtio: number)
```

Sets the text zoom ratio of the page.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [textZoomRatio](#textzoomratio)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textZoomAtio | number | Yes | Text zoom percentage of the page to set. The value 100 indicates the original size, a value greater than 100 indicates zoom-in, and a value less than 100 indicates zoom-out. The value range is (0, 2147483647]. |

**Examples**

```TypeScript
// xxx.ets
@Entry
@Component
struct WebComponent {
  controller: WebController = new WebController()
  @State ratio: number = 150
  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .textZoomAtio(this.ratio)
    }
  }
}
```

## textZoomRatio

```TypeScript
textZoomRatio(textZoomRatio: number)
```

Sets the text zoom ratio of the page. When this attribute is not explicitly called, the default zoom ratio is 100%.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textZoomRatio | number | Yes | Text zoom percentage for the page. The value **100** indicates the original size, a value greater than **100** indicates zoom in, and a value less than **100** indicates zoom out. The value is an integer in the range (0, 2147483647]. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State ratio: number = 150;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .textZoomRatio(this.ratio)
    }
  }
}
```

## userAgent

```TypeScript
userAgent(userAgent: string)
```

Sets the user agent.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** setCustomUserAgent

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| userAgent | string | Yes | User agent to set. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State userAgent:string = 'Mozilla/5.0 (Phone; OpenHarmony 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 ArkWeb/4.1.6.1 Mobile DemoApp';

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .userAgent(this.userAgent)
    }
  }
}
```

## verticalScrollBarAccess

```TypeScript
verticalScrollBarAccess(verticalScrollBar: boolean)
```

Sets whether to display the vertical scrollbar, including the system default scrollbar and user-defined scrollbars. If this attribute is not explicitly called, the scrollbar is displayed by default.

> **NOTE：**
> 
> - If an @State decorated variable is used to control the vertical scrollbar visibility, **controller.refresh()**
> must be called for the settings to take effect.
> 
> - If the vertical scrollbar visibility changes frequently through an @State decorated variable, it is recommended
> that the variable correspond to the **Web** component one by one.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| verticalScrollBar | boolean | Yes | Whether to display the vertical scrollbar. The value **true** means to display, and **false** means not to display. The default value is **false** when undefined or null is passed in. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State isShow: boolean = true;
  @State btnMsg: string = 'Hide scrollbar';

  build() {
    Column() {
      // If an @State decorated variable is used to control the vertical scrollbar visibility, controller.refresh() must be called for the settings to take effect.
      Button(this.btnMsg)
        .onClick(() => {
          if (this.isShow) {
            this.isShow = false;
            this.btnMsg = 'Show scrollbar';
          } else {
            this.isShow = true;
            this.btnMsg = 'Hide scrollbar';
          }
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`Failed to refresh Web. Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}`);
          }
        }).height('10%').width('40%')
      Web({ src: $rawfile('index.html'), controller: this.controller }).height('90%')
        .verticalScrollBarAccess(this.isShow)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1.0">
    <title>Demo</title>
    <style>
        body {
          width:3000px;
          height:6000px;
          padding-right:170px;
          padding-left:170px;
          border:5px solid blueviolet;
        }
    </style>
</head>
<body>
Scroll Test
</body>
</html>
```

## webCursiveFont

```TypeScript
webCursiveFont(family: string)
```

Sets the cursive font family of the web page to render HTML elements that use the **cursive** font.

When this attribute is not explicitly called, the default cursive font family of the web page is **cursive**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string | Yes | Cursive font family to set. When **null** or **undefined** is passed in, the value is **cursive**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "cursive";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webCursiveFont(this.family)
    }
  }
}
```

## webFantasyFont

```TypeScript
webFantasyFont(family: string)
```

Sets the fantasy font family of the web page to render HTML elements that use the **fantasy** font.

When this attribute is not explicitly called, the default fantasy font family of the web page is **fantasy**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string | Yes | Fantasy font family to set. When **null** or **undefined** is passed in, the value is **fantasy**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "fantasy";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webFantasyFont(this.family)
    }
  }
}
```

## webFixedFont

```TypeScript
webFixedFont(family: string)
```

Sets the fixed font family of the web page to render HTML elements that use the **monospace** font.

When this attribute is not explicitly called, the default fixed font family of the web page is **monospace**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string | Yes | Fixed font family for web pages. The value is a font name string, for example, "monospace" or "Arial". The value **monospace** is used when null or undefined is passed. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "monospace";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webFixedFont(this.family)
    }
  }
}
```

## webSansSerifFont

```TypeScript
webSansSerifFont(family: string)
```

Sets the sans-serif font family of the web page to render HTML elements that use the **sans-serif** font.

When this attribute is not explicitly called, the sans-serif font family of the web page is **sans-serif** by default.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string | Yes | Sans-serif font family to set. When **null** or **undefined** is passed in, the sans-serif font family is **sans-serif**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "sans-serif";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webSansSerifFont(this.family)
    }
  }
}
```

## webSerifFont

```TypeScript
webSerifFont(family: string)
```

Sets the serif font family of the web page to render HTML elements that use the **serif** font.

When this attribute is not explicitly called, the default serif font family of the web page is **serif**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string | Yes | Serif font family to set. When **null** or **undefined** is passed in, the sans-serif font family is **serif**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "serif";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webSerifFont(this.family)
    }
  }
}
```

## webStandardFont

```TypeScript
webStandardFont(family: string)
```

Sets the standard font family of the web page to render HTML elements whose font style is not specified.

When this attribute is not explicitly called, the default standard font family of the web page is **sans-serif**.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string | Yes | Standard font family to set. When **null** or **undefined** is passed in, the sans-serif font family is **sans-serif**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State family: string = "sans-serif";

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .webStandardFont(this.family)
    }
  }
}
```

## wideViewModeAccess

```TypeScript
wideViewModeAccess(wideViewModeAccess: boolean)
```

Sets whether to support the **viewport** attribute of the HTML **\&lt;meta&gt;** tag. This API is an empty API.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** [metaViewport](#metaviewport)

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| wideViewModeAccess | boolean | Yes | Whether to support the **viewport** attribute of the HTML **&lt;meta&gt;** tag. The value **true** means to support the **viewport** attribute of the HTML **&lt;meta&gt;** tag, and **false** means the opposite. |

## zoomAccess

```TypeScript
zoomAccess(zoomAccess: boolean)
```

Sets whether to support zoom gestures. If this attribute is not explicitly called, zoom gestures are supported by default.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoomAccess | boolean | Yes | Whether to support gesture-based zooming. The value **true** indicates supported, and **false** indicates not supported. When **undefined** or **null** is passed, the value is **false**. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .zoomAccess(true)
    }
  }
}
```

## zoomControlAccess

```TypeScript
zoomControlAccess(zoomControlAccess: boolean)
```

Sets whether to allow zooming by pressing **Ctrl + '-/+'** or **Ctrl** + mouse wheel/touchpad.

If this attribute is not explicitly called, zooming by pressing **Ctrl + '-/+'** or **Ctrl** + mouse wheel/touchpad is allowed by default.

**Since:** 22

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoomControlAccess | boolean | Yes | Whether to allow zooming through key combinations. The value **true** means the zooming is supported, and **false** means the opposite. If null or undefined is passed, the default value **false** is used. |

**Examples**

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .zoomControlAccess(true)
    }
  }
}
```

HTML file to be loaded:

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Test Web Page</title>
</head>
<body>
  <h1>zoomControlAccess Demo</h1>
  <span>You can zoom in/out page when zoomControlAccess is true.</span>
</body>
</html>
```
