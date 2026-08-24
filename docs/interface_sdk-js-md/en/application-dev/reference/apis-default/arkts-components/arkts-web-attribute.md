# WebAttribute

Defines the Web attribute functions.@extends CommonMethod&lt;WebAttribute&gt;

**Inheritance/Implementation:** WebAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface WebAttribute--><!--Device-unnamed-export declare interface WebAttribute-End-->

**System capability:** SystemCapability.Web.Webview.Core

## aiSessionOptions

```TypeScript
aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this--><!--Device-WebAttribute-aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| aiSessions | Array&lt;[AISessionEvent](arkts-web-aisessionevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## allowWindowOpenMethod

```TypeScript
allowWindowOpenMethod(flag: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-allowWindowOpenMethod(flag: boolean | undefined): this--><!--Device-WebAttribute-allowWindowOpenMethod(flag: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| flag | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
                    // To display the web page to the foreground, the application should perform a tab or window switch.
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
                    // If the event.handler.setWebController API is not called, the render process will be blocked.
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

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-WebAttribute-attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[WebAttribute](arkts-web-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## backToTop

```TypeScript
backToTop(backToTop: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-backToTop(backToTop: boolean | undefined): this--><!--Device-WebAttribute-backToTop(backToTop: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| backToTop | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this--><!--Device-WebAttribute-bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementType | [WebElementType](arkts-web-webelementtype-e.md) \| undefined | Yes |  |
| content | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined | Yes |  |
| responseType | [WebResponseType](arkts-web-webresponsetype-e.md) \| undefined | Yes |  |
| options | [SelectionMenuOptionsExt](arkts-web-selectionmenuoptionsext-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
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
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
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
blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this--><!--Device-WebAttribute-blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| detectConfig | [BlankScreenDetectionConfig](arkts-web-blankscreendetectionconfig-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
blockNetwork(block: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-blockNetwork(block: boolean | undefined): this--><!--Device-WebAttribute-blockNetwork(block: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| block | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this--><!--Device-WebAttribute-blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [BlurOnKeyboardHideMode](arkts-web-bluronkeyboardhidemode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this--><!--Device-WebAttribute-bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| condition | [WebBypassVsyncCondition](arkts-web-webbypassvsynccondition-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
cacheMode(cacheMode: CacheMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-cacheMode(cacheMode: CacheMode | undefined): this--><!--Device-WebAttribute-cacheMode(cacheMode: CacheMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cacheMode | [CacheMode](arkts-web-cachemode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
copyOptions(value: CopyOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-copyOptions(value: CopyOptions | undefined): this--><!--Device-WebAttribute-copyOptions(value: CopyOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CopyOptions](../../apis-arkui/arkts-apis/arkts-arkui-copyoptions-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
darkMode(mode: WebDarkMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-darkMode(mode: WebDarkMode | undefined): this--><!--Device-WebAttribute-darkMode(mode: WebDarkMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebDarkMode](arkts-web-webdarkmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
databaseAccess(databaseAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-databaseAccess(databaseAccess: boolean | undefined): this--><!--Device-WebAttribute-databaseAccess(databaseAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| databaseAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
dataDetectorConfig(config: TextDataDetectorConfig | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-dataDetectorConfig(config: TextDataDetectorConfig | undefined): this--><!--Device-WebAttribute-dataDetectorConfig(config: TextDataDetectorConfig | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [TextDataDetectorConfig](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textdatadetectorconfig-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
defaultFixedFontSize(size: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-defaultFixedFontSize(size: int | undefined): this--><!--Device-WebAttribute-defaultFixedFontSize(size: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
defaultFontSize(size: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-defaultFontSize(size: int | undefined): this--><!--Device-WebAttribute-defaultFontSize(size: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
defaultTextEncodingFormat(textEncodingFormat: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-defaultTextEncodingFormat(textEncodingFormat: string | undefined): this--><!--Device-WebAttribute-defaultTextEncodingFormat(textEncodingFormat: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textEncodingFormat | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
domStorageAccess(domStorageAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-domStorageAccess(domStorageAccess: boolean | undefined): this--><!--Device-WebAttribute-domStorageAccess(domStorageAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| domStorageAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-editMenuOptions(editMenu: EditMenuOptions | undefined): this--><!--Device-WebAttribute-editMenuOptions(editMenu: EditMenuOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| editMenu | [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-editmenuoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
      return true; // Return true to not execute the system callback.
    } else if (menuItem.id.equals(TextMenuItemId.COPY)) {
      // Custom behavior
      console.info("Not intercept ID: COPY")
      return false; // Return false to execute the system callback.
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
enableAutoFill(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableAutoFill(value: boolean | undefined): this--><!--Device-WebAttribute-enableAutoFill(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
enableDataDetector(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableDataDetector(enable: boolean | undefined): this--><!--Device-WebAttribute-enableDataDetector(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
enableDefaultContextMenu(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableDefaultContextMenu(enable: boolean | undefined): this--><!--Device-WebAttribute-enableDefaultContextMenu(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableDrag

```TypeScript
enableDrag(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableDrag(value: boolean | undefined): this--><!--Device-WebAttribute-enableDrag(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableFollowSystemFontWeight

```TypeScript
enableFollowSystemFontWeight(follow: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableFollowSystemFontWeight(follow: boolean | undefined): this--><!--Device-WebAttribute-enableFollowSystemFontWeight(follow: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| follow | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
enableFullscreenVideoOverlay(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableFullscreenVideoOverlay(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableFullscreenVideoOverlay(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableHapticFeedback

```TypeScript
enableHapticFeedback(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableHapticFeedback(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableHapticFeedback(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
enableImageAnalyzer(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableImageAnalyzer(enable: boolean | undefined): this--><!--Device-WebAttribute-enableImageAnalyzer(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
enableMediaNetworkProxy(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableMediaNetworkProxy(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableMediaNetworkProxy(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableNativeEmbedMode

```TypeScript
enableNativeEmbedMode(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableNativeEmbedMode(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableNativeEmbedMode(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this--><!--Device-WebAttribute-enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [NativeMediaPlayerConfig](arkts-web-nativemediaplayerconfig-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this--><!--Device-WebAttribute-enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |
| type | [ScrollDirectionalLockType](arkts-web-scrolldirectionallocktype-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableSelectedDataDetector

```TypeScript
enableSelectedDataDetector(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableSelectedDataDetector(enable: boolean | undefined): this--><!--Device-WebAttribute-enableSelectedDataDetector(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
enableWebAVSession(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-enableWebAVSession(enabled: boolean | undefined): this--><!--Device-WebAttribute-enableWebAVSession(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
fileAccess(fileAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-fileAccess(fileAccess: boolean | undefined): this--><!--Device-WebAttribute-fileAccess(fileAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fileAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
forceDarkAccess(access: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-forceDarkAccess(access: boolean | undefined): this--><!--Device-WebAttribute-forceDarkAccess(access: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| access | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
forceDisplayScrollBar(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-forceDisplayScrollBar(enabled: boolean | undefined): this--><!--Device-WebAttribute-forceDisplayScrollBar(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
forceEnableZoom(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-forceEnableZoom(enable: boolean | undefined): this--><!--Device-WebAttribute-forceEnableZoom(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
geolocationAccess(geolocationAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-geolocationAccess(geolocationAccess: boolean | undefined): this--><!--Device-WebAttribute-geolocationAccess(geolocationAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| geolocationAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
gestureFocusMode(mode: GestureFocusMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-gestureFocusMode(mode: GestureFocusMode | undefined): this--><!--Device-WebAttribute-gestureFocusMode(mode: GestureFocusMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [GestureFocusMode](arkts-web-gesturefocusmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this--><!--Device-WebAttribute-horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| horizontalScrollBar | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
  @State btnMsg: string ="Hide the scrollbar";

  build() {
    Column() {
      // If an @State decorated variable is used to control the horizontal scrollbar visibility, controller.refresh() must be called for the settings to take effect.
      Button('refresh')
        .onClick(() => {
          if(this.isShow){
            this.isShow = false;
            this.btnMsg="Display the scrollbar";
          }else{
            this.isShow = true;
            this.btnMsg="Hide the scrollbar";
          }
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        }).height("10%").width("40%")
      Web({ src: $rawfile('index.html'), controller: this.controller }).height("90%")
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
imageAccess(imageAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-imageAccess(imageAccess: boolean | undefined): this--><!--Device-WebAttribute-imageAccess(imageAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| imageAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
initialScale(percent: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-initialScale(percent: double | undefined): this--><!--Device-WebAttribute-initialScale(percent: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| percent | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
javaScriptAccess(javaScriptAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-javaScriptAccess(javaScriptAccess: boolean | undefined): this--><!--Device-WebAttribute-javaScriptAccess(javaScriptAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| javaScriptAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## javaScriptProxy

```TypeScript
javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this--><!--Device-WebAttribute-javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| javaScriptProxy | [JavaScriptProxy](arkts-web-javascriptproxy-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this--><!--Device-WebAttribute-keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebKeyboardAppearanceMode](arkts-web-webkeyboardappearancemode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## keyboardAvoidMode

```TypeScript
keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this--><!--Device-WebAttribute-keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebKeyboardAvoidMode](arkts-web-webkeyboardavoidmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
layoutMode(mode: WebLayoutMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-layoutMode(mode: WebLayoutMode | undefined): this--><!--Device-WebAttribute-layoutMode(mode: WebLayoutMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [WebLayoutMode](arkts-web-weblayoutmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
mediaOptions(options: WebMediaOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-mediaOptions(options: WebMediaOptions | undefined): this--><!--Device-WebAttribute-mediaOptions(options: WebMediaOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [WebMediaOptions](arkts-web-webmediaoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
mediaPlayGestureAccess(access: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-mediaPlayGestureAccess(access: boolean | undefined): this--><!--Device-WebAttribute-mediaPlayGestureAccess(access: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| access | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
metaViewport(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-metaViewport(enabled: boolean | undefined): this--><!--Device-WebAttribute-metaViewport(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
minFontSize(size: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-minFontSize(size: int | undefined): this--><!--Device-WebAttribute-minFontSize(size: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
minLogicalFontSize(size: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-minLogicalFontSize(size: int | undefined): this--><!--Device-WebAttribute-minLogicalFontSize(size: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| size | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
mixedMode(mixedMode: MixedMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-mixedMode(mixedMode: MixedMode | undefined): this--><!--Device-WebAttribute-mixedMode(mixedMode: MixedMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mixedMode | [MixedMode](arkts-web-mixedmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
multiWindowAccess(multiWindow: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-multiWindowAccess(multiWindow: boolean | undefined): this--><!--Device-WebAttribute-multiWindowAccess(multiWindow: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| multiWindow | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## nativeEmbedOptions

```TypeScript
nativeEmbedOptions(options?: EmbedOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-nativeEmbedOptions(options?: EmbedOptions | undefined): this--><!--Device-WebAttribute-nativeEmbedOptions(options?: EmbedOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [EmbedOptions](arkts-web-embedoptions-i.md) \| undefined | No |  |

**Return value:**

| Type | Description |
| --- | --- |
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
nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this--><!--Device-WebAttribute-nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| [NestedScrollOptionsExt](arkts-web-nestedscrolloptionsext-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onActivateContent(callback: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onActivateContent(callback: VoidCallback | undefined): this--><!--Device-WebAttribute-onActivateContent(callback: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this--><!--Device-WebAttribute-onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnAdsBlockedCallback](arkts-onadsblockedcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this--><!--Device-WebAttribute-onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnAlertEvent](arkts-web-onalertevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this--><!--Device-WebAttribute-onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnAudioStateChangedEvent](arkts-web-onaudiostatechangedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this--><!--Device-WebAttribute-onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnBeforeUnloadEvent](arkts-web-onbeforeunloadevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this--><!--Device-WebAttribute-onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnCameraCaptureStateChangeCallback](arkts-oncameracapturestatechangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this--><!--Device-WebAttribute-onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnClientAuthenticationEvent](arkts-web-onclientauthenticationevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this--><!--Device-WebAttribute-onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnConfirmEvent](arkts-web-onconfirmevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this--><!--Device-WebAttribute-onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnConsoleEvent](arkts-web-onconsoleevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this--><!--Device-WebAttribute-onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnContextMenuHideCallback](arkts-oncontextmenuhidecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this--><!--Device-WebAttribute-onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnContextMenuShowEvent](arkts-web-oncontextmenushowevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onControllerAttached(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onControllerAttached(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onControllerAttached(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this--><!--Device-WebAttribute-onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnDataResubmittedEvent](arkts-web-ondataresubmittedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this--><!--Device-WebAttribute-onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnDetectBlankScreenCallback](arkts-ondetectblankscreencallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this--><!--Device-WebAttribute-onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnDownloadStartEvent](arkts-web-ondownloadstartevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this--><!--Device-WebAttribute-onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnErrorReceiveEvent](arkts-web-onerrorreceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this--><!--Device-WebAttribute-onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnFaviconReceivedEvent](arkts-web-onfaviconreceivedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## onFirstContentfulPaint

```TypeScript
onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this--><!--Device-WebAttribute-onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnFirstContentfulPaintEvent](arkts-web-onfirstcontentfulpaintevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this--><!--Device-WebAttribute-onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFirstMeaningfulPaintCallback](arkts-onfirstmeaningfulpaintcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this--><!--Device-WebAttribute-onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFirstScreenPaintCallback](arkts-onfirstscreenpaintcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this--><!--Device-WebAttribute-onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnFullScreenEnterCallback](arkts-onfullscreenentercallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onFullScreenExit(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onFullScreenExit(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onFullScreenExit(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onGeolocationHide(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onGeolocationHide(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onGeolocationHide(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this--><!--Device-WebAttribute-onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnGeolocationShowEvent](arkts-web-ongeolocationshowevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this--><!--Device-WebAttribute-onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnHttpAuthRequestEvent](arkts-web-onhttpauthrequestevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this--><!--Device-WebAttribute-onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnHttpErrorReceiveEvent](arkts-web-onhttperrorreceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this--><!--Device-WebAttribute-onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnInputmethodAttachedCallback](arkts-oninputmethodattachedcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onIntelligentTrackingPreventionResult

```TypeScript
onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this--><!--Device-WebAttribute-onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnIntelligentTrackingPreventionCallback](arkts-onintelligenttrackingpreventioncallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this--><!--Device-WebAttribute-onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [WebKeyboardCallback](arkts-webkeyboardcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this--><!--Device-WebAttribute-onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((event: KeyEvent) =&gt; boolean) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this--><!--Device-WebAttribute-onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnInterceptRequestEvent](arkts-web-oninterceptrequestevent-i.md), [WebResourceResponse](arkts-web-webresourceresponse-c.md) \| null&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this--><!--Device-WebAttribute-onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnLargestContentfulPaintCallback](arkts-onlargestcontentfulpaintcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onlineImageAccess(onlineImageAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onlineImageAccess(onlineImageAccess: boolean | undefined): this--><!--Device-WebAttribute-onlineImageAccess(onlineImageAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| onlineImageAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this--><!--Device-WebAttribute-onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadFinishedEvent](arkts-web-onloadfinishedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this--><!--Device-WebAttribute-onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadInterceptEvent](arkts-web-onloadinterceptevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this--><!--Device-WebAttribute-onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadStartedEvent](arkts-web-onloadstartedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this--><!--Device-WebAttribute-onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnMicrophoneCaptureStateChangeCallback](arkts-onmicrophonecapturestatechangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this--><!--Device-WebAttribute-onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((event: NativeEmbedTouchInfo) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this--><!--Device-WebAttribute-onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | ((event: NativeEmbedDataInfo) =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [MouseInfoCallback](arkts-mouseinfocallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedObjectParamChangeCallback](arkts-onnativeembedobjectparamchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this--><!--Device-WebAttribute-onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNativeEmbedVisibilityChangeCallback](arkts-onnativeembedvisibilitychangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this--><!--Device-WebAttribute-onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnNavigationEntryCommittedCallback](arkts-onnavigationentrycommittedcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this--><!--Device-WebAttribute-onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnOverrideErrorPageCallback](arkts-onoverrideerrorpagecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this--><!--Device-WebAttribute-onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnOverrideUrlLoadingCallback](arkts-onoverrideurlloadingcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this--><!--Device-WebAttribute-onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnOverScrollEvent](arkts-web-onoverscrollevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this--><!--Device-WebAttribute-onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageBeginEvent](arkts-web-onpagebeginevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this--><!--Device-WebAttribute-onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageEndEvent](arkts-web-onpageendevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this--><!--Device-WebAttribute-onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageVisibleEvent](arkts-web-onpagevisibleevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this--><!--Device-WebAttribute-onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPdfLoadEvent](arkts-web-onpdfloadevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this--><!--Device-WebAttribute-onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPdfScrollEvent](arkts-web-onpdfscrollevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this--><!--Device-WebAttribute-onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPermissionRequestEvent](arkts-web-onpermissionrequestevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this--><!--Device-WebAttribute-onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnProgressChangeEvent](arkts-web-onprogresschangeevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this--><!--Device-WebAttribute-onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPromptEvent](arkts-web-onpromptevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this--><!--Device-WebAttribute-onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnRefreshAccessedHistoryEvent](arkts-web-onrefreshaccessedhistoryevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this--><!--Device-WebAttribute-onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnRenderExitedEvent](arkts-web-onrenderexitedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## onRenderProcessNotResponding

```TypeScript
onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this--><!--Device-WebAttribute-onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRenderProcessNotRespondingCallback](arkts-onrenderprocessnotrespondingcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this--><!--Device-WebAttribute-onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRenderProcessRespondingCallback](arkts-onrenderprocessrespondingcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onRequestSelected(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onRequestSelected(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onRequestSelected(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this--><!--Device-WebAttribute-onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnResourceLoadEvent](arkts-web-onresourceloadevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this--><!--Device-WebAttribute-onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-onsafebrowsingcheckresultcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this--><!--Device-WebAttribute-onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-onsafebrowsingcheckresultcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this--><!--Device-WebAttribute-onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScaleChangeEvent](arkts-web-onscalechangeevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this--><!--Device-WebAttribute-onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScreenCaptureRequestEvent](arkts-web-onscreencapturerequestevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onScroll(callback: Callback<OnScrollEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onScroll(callback: Callback<OnScrollEvent> | undefined): this--><!--Device-WebAttribute-onScroll(callback: Callback<OnScrollEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScrollEvent](arkts-web-onscrollevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this--><!--Device-WebAttribute-onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnSearchResultReceiveEvent](arkts-web-onsearchresultreceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this--><!--Device-WebAttribute-onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnShowFileSelectorEvent](arkts-web-onshowfileselectorevent-i.md), boolean&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this--><!--Device-WebAttribute-onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnSslErrorEventCallback](arkts-onsslerroreventcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this--><!--Device-WebAttribute-onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnSslErrorEventReceiveEvent](arkts-web-onsslerroreventreceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## onTextSelectionChange

```TypeScript
onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this--><!--Device-WebAttribute-onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [TextSelectionChangeCallback](arkts-textselectionchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this--><!--Device-WebAttribute-onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnTitleReceiveEvent](arkts-web-ontitlereceiveevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this--><!--Device-WebAttribute-onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnTouchIconUrlReceivedEvent](arkts-web-ontouchiconurlreceivedevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## onVerifyPin

```TypeScript
onVerifyPin(callback: OnVerifyPinCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onVerifyPin(callback: OnVerifyPinCallback | undefined): this--><!--Device-WebAttribute-onVerifyPin(callback: OnVerifyPinCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnVerifyPinCallback](arkts-onverifypincallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this--><!--Device-WebAttribute-onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnViewportFitChangedCallback](arkts-onviewportfitchangedcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onWindowExit(callback: (() => void) | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onWindowExit(callback: (() => void) | undefined): this--><!--Device-WebAttribute-onWindowExit(callback: (() => void) | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | (() =&gt; void) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this--><!--Device-WebAttribute-onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnWindowNewEvent](arkts-web-onwindownewevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this--><!--Device-WebAttribute-onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnWindowNewExtEvent](arkts-web-onwindownewextevent-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
optimizeParserBudget(optimizeParserBudget: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-optimizeParserBudget(optimizeParserBudget: boolean | undefined): this--><!--Device-WebAttribute-optimizeParserBudget(optimizeParserBudget: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| optimizeParserBudget | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
overScrollMode(mode: OverScrollMode | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-overScrollMode(mode: OverScrollMode | undefined): this--><!--Device-WebAttribute-overScrollMode(mode: OverScrollMode | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| mode | [OverScrollMode](arkts-web-overscrollmode-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
overviewModeAccess(overviewModeAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-overviewModeAccess(overviewModeAccess: boolean | undefined): this--><!--Device-WebAttribute-overviewModeAccess(overviewModeAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| overviewModeAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## pinchSmooth

```TypeScript
pinchSmooth(isEnabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-pinchSmooth(isEnabled: boolean | undefined): this--><!--Device-WebAttribute-pinchSmooth(isEnabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isEnabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this--><!--Device-WebAttribute-registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tag | string \| undefined | Yes |  |
| type | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
rotateRenderEffect(effect: WebRotateEffect | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-rotateRenderEffect(effect: WebRotateEffect | undefined): this--><!--Device-WebAttribute-rotateRenderEffect(effect: WebRotateEffect | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| effect | [WebRotateEffect](arkts-web-webrotateeffect-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## runJavaScriptOnHeadEnd

```TypeScript
runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this--><!--Device-WebAttribute-runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-web-scriptitem-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this--><!--Device-WebAttribute-scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| policy | [ScrollbarLayoutPolicy](arkts-web-scrollbarlayoutpolicy-e.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## textAutosizing

```TypeScript
textAutosizing(textAutosizing: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-textAutosizing(textAutosizing: boolean | undefined): this--><!--Device-WebAttribute-textAutosizing(textAutosizing: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textAutosizing | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## textZoomRatio

```TypeScript
textZoomRatio(textZoomRatio: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-textZoomRatio(textZoomRatio: int | undefined): this--><!--Device-WebAttribute-textZoomRatio(textZoomRatio: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| textZoomRatio | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## verticalScrollBarAccess

```TypeScript
verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this--><!--Device-WebAttribute-verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| verticalScrollBar | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
  @State btnMsg: string ="Hide the scrollbar";

  build() {
    Column() {
      // If an @State decorated variable is used to control the vertical scrollbar visibility, controller.refresh() must be called for the settings to take effect.
      Button(this.btnMsg)
        .onClick(() => {
          if(this.isShow){
            this.isShow = false;
            this.btnMsg="Display the scrollbar";
          }else{
            this.isShow = true;
            this.btnMsg="Hide the scrollbar";
          }
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        }).height("10%").width("40%")
      Web({ src: $rawfile('index.html'), controller: this.controller }).height("90%")
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
webCursiveFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-webCursiveFont(family: string | undefined): this--><!--Device-WebAttribute-webCursiveFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
webFantasyFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-webFantasyFont(family: string | undefined): this--><!--Device-WebAttribute-webFantasyFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
webFixedFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-webFixedFont(family: string | undefined): this--><!--Device-WebAttribute-webFixedFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
webSansSerifFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-webSansSerifFont(family: string | undefined): this--><!--Device-WebAttribute-webSansSerifFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
webSerifFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-webSerifFont(family: string | undefined): this--><!--Device-WebAttribute-webSerifFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
webStandardFont(family: string | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-webStandardFont(family: string | undefined): this--><!--Device-WebAttribute-webStandardFont(family: string | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| family | string \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## zoomAccess

```TypeScript
zoomAccess(zoomAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-zoomAccess(zoomAccess: boolean | undefined): this--><!--Device-WebAttribute-zoomAccess(zoomAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoomAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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
zoomControlAccess(zoomControlAccess: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-WebAttribute-zoomControlAccess(zoomControlAccess: boolean | undefined): this--><!--Device-WebAttribute-zoomControlAccess(zoomControlAccess: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| zoomControlAccess | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
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

## default

```TypeScript
default
```

Set whether to enable media network proxy for Web components. When enabled, network requests for media resources are routed through the web components network stack. This attribute takes effect for HLS media, other media formats are unaffected.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebAttribute-default--><!--Device-WebAttribute-default-End-->

**System capability:** SystemCapability.Web.Webview.Core

