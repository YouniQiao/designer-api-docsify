# WebAttribute

Defines the Web attribute functions.@extends CommonMethod&lt;WebAttribute&gt;

**继承/实现关系：** WebAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## aiSessionOptions

```TypeScript
default aiSessionOptions(aiSessions: Array<AISessionEvent> | undefined): this
```

Custom AI session configuration for Web components. Used to register multiple custom AI sessions.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| aiSessions | Array&lt;[AISessionEvent](arkts-arkweb-web-aisessionevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct DemoPage {
  private webController: webview.WebviewController = new webview.WebviewController();
  sessions: Map<string, string> = new Map<string, string>();

  onCreateAISession = (id: string, params: string, result: OnAISessionCallback): boolean => {
    this.sessions.set(id, params); // 模拟创建AI会话
    console.info(`[AISession]onCreateAISession params: ${params}`);
    // 通知调用方AI会话创建成功
    result(AISessionResultType.SUCCESS, "AISession created");
    return true;
  }

  onExecuteAIAction = (id: string, params: string, result: OnAISessionCallback): void => {
    this.sessions.get(id); // 模拟取出会话，并执行动作
    console.info(`[AISession]onExecuteAIAction params: ${params}`);
    // 模拟流式返回AI执行结果：多次调用RUNNING表示任务执行中、返回数据块，最后返回SUCCESS表示任务完成
    result(AISessionResultType.RUNNING, "AISession chunk 1\n");
    result(AISessionResultType.RUNNING, "AISession chunk 2\n");
    result(AISessionResultType.SUCCESS, "AISession chunk end\n");
  }

  onDestroyAISession = (id: string): void => {
    this.sessions.delete(id); // 模拟销毁会话并释放资源
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

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import {
  $rawfile,
  AISessionEvent,
  AISessionResultType,
  AISessionType,
  Column,
  Component,
  Entry,
  OnAISessionCallback,
  Web
} from '@ohos.arkui.component';
import webview from '@ohos.web.webview';

@Entry
@Component
struct Index {
  webController: webview.WebviewController = new webview.WebviewController(undefined)
  sessions: Map<string, string> = new Map<string, string>();
  options: AISessionEvent = {
    aiSessionType: AISessionType.SUMMARIZER,
    onCreateAISession: (id: string, params: string, result: OnAISessionCallback): boolean => {
      this.sessions.set(id, params); // 模拟创建AI会话
      console.info(`[AISession]onCreateAISession params: ${params}`);
      // 通知调用方AI会话创建成功
      result(AISessionResultType.SUCCESS, "AISession created");
      return true;
    },
    onExecuteAIAction: (id: string, params: string, result: OnAISessionCallback): void => {
      this.sessions.get(id); // 模拟取出会话，并执行动作
      console.info(`[AISession]onExecuteAIAction params: ${params}`);
      // 模拟流式返回AI执行结果：多次调用RUNNING表示任务执行中、返回数据块，最后返回SUCCESS表示任务完成
      result(AISessionResultType.RUNNING, "AISession chunk 1\n");
      result(AISessionResultType.RUNNING, "AISession chunk 2\n");
      result(AISessionResultType.SUCCESS, "AISession chunk end\n");
    },
    onDestroyAISession: (id: string): void => {
      this.sessions.delete(id); // 模拟销毁会话并释放资源
    }
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

加载的html文件

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
default allowWindowOpenMethod(flag: boolean | undefined): this
```

Whether the window can be open automatically through JavaScript. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> This API takes effect only when JavaScript is enabled. This API opens a new window when [multiWindowAccess](#multiwindowaccess) is enabled and opens a local window when [multiWindowAccess](#multiwindowaccess) is disabled. The default value of **flag** is subject to the settings of the **persist.web.allowWindowOpenMethod.enabled** system attribute. If this attribute is not set, the default value of **flag** is **false**. To check the settings of **persist.web.allowWindowOpenMethod.enabled**, run the **hdc shell param get persist.web.allowWindowOpenMethod.enabled** command. If the attribute value is 1, it means the system attribute is enabled; If the attribute value is 0 or does not exist, it means that the system attribute has not been enabled. you can run the **hdc shell param set persist.web.allowWindowOpenMethod.enabled 1** command to enable it. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| flag | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

// 在同一界面有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
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
                    // 该Web需要展示到前台，建议应用在这里进行tab或window切换的动作
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
                // 需要使能multiWindowAccess
                .multiWindowAccess(true)
                .allowWindowOpenMethod(true)
                .onWindowNew((event) => {
                    if (this.dialogController) {
                        this.dialogController.close()
                    }
                    let popController: webview.WebviewController = new webview.WebviewController();
                    // 将新窗口对应WebviewController返回给Web内核。
                    // 若不调用event.handler.setWebController接口，会造成渲染进程阻塞。
                    // 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
                    event.handler.setWebController(popController);
                    this.dialogController = new CustomDialogController({
                        builder: NewWebViewComp({ webviewController1: popController }),
                        // isModal设置为false，防止新窗口被销毁而无法触发onActivateContent回调
                        isModal: false
                    })
                    this.dialogController.open();
                })
        }
    }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Component, Entry, Web, Column, CustomDialogController, CustomDialog } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

// 在同一界面有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
@CustomDialog
struct NewWebViewComp {
  controller?: CustomDialogController;
  webviewController1: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: "", controller: this.webviewController1 })
        .javaScriptAccess(true)
        .multiWindowAccess(false)
        .onWindowExit(() => {
          console.info("NewWebViewComp onWindowExit");
          if (this.controller) {
            this.controller?.close();
          }
        })
        .onActivateContent(() => {
            //该Web需要展示到前台，建议应用在这里进行tab或window切换的动作。
            console.info("NewWebViewComp onActivateContent")
        })
    }
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  dialogController: CustomDialogController | null = null;

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .javaScriptAccess(true)
        // 需要使能multiWindowAccess。
        .multiWindowAccess(true)
        .allowWindowOpenMethod(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController?.close();
          }
          let popController: webview.WebviewController = new webview.WebviewController(undefined);
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController }),
            // isModal设置为false，防止新窗口被销毁而无法触发onActivateContent回调。
            isModal: false
          })
          this.dialogController?.open();
          // 将新窗口对应WebviewController返回给Web内核。
          // 若不调用event.handler.setWebController接口，会造成render进程阻塞。
          // 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
          event.handler.setWebController(popController);
        })
    }
  }
}
```

HTML示例：

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
default attributeModifier(modifier: AttributeModifier<WebAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[WebAttribute](arkts-arkweb-web-webattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

## backToTop

```TypeScript
default backToTop(backToTop: boolean | undefined): this
```

Set whether to enable the back-to-top feature for web component when the status bar is touched.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [backToTop](#backtotop) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// backToTop.ets
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, $rawfile} from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .backToTop(true)
    }
  }
}
```

加载的html文件：

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
         text-align: center;       /* 水平居中 */
         line-height: 200px;       /* 垂直居中（值等于容器高度） */
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
default bindSelectionMenu(elementType: WebElementType | undefined, content: CustomBuilder | undefined, responseType: WebResponseType | undefined, options?: SelectionMenuOptionsExt | undefined): this
```

Bind to the selection menu.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| elementType | [WebElementType](arkts-arkweb-web-webelementtype-e.md) \| undefined | 是 |
| content | [CustomBuilder](../../apis-arkui/arkts-apis/arkts-arkui-custombuilder-t.md) \| undefined | 是 |
| responseType | [WebResponseType](arkts-arkweb-web-webresponsetype-e.md) \| undefined | 是 |
| options | [SelectionMenuOptionsExt](arkts-arkweb-web-selectionmenuoptionsext-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
        Text("") // 可选择是否展示url
          .padding(5)
          .width('100%')
          .textAlign(TextAlign.Start)
          .backgroundColor(Color.White)
          .copyOption(CopyOptions.LocalDevice)
          .maxLines(1)
          .textOverflow({overflow:TextOverflow.Ellipsis})
        Progress({ value: this.progressValue, total: 100, type: ProgressType.Linear }) // 展示进度条
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
        .hitTestBehavior(HitTestMode.None) // 使预览Web不响应手势
    }.width($$.width).height($$.height) // 设置预览宽高
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
      MenuItem({ content: '复制链接', })
        .onClick(() => {
          const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, this.linkURL);
          const systemPasteboard = pasteboard.getSystemPasteboard();
          systemPasteboard.setData(pasteboardData);
        })
      MenuItem({content:'打开链接'})
        .onClick(()=>{
          this.controller.loadUrl(this.linkURL);
        })
    }
  }
  @Builder
  ImageMenuBuilder() {
    Menu() {
      MenuItem({ content: '复制图片', })
        .onClick(() => {
          this.result?.copyImage();
          this.result?.closeContextMenu();
        })
    }
  }
  @Builder
  TextMenuBuilder() {
    Menu() {
      MenuItem({ content: '复制', })
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
            // 返回true表示拦截系统默认的上下文菜单，使用自定义菜单
            return true;
          }
          return false;
        })
    }

  }
  // 侧滑返回
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { $rawfile, Web, Column, Component, Entry, Image, ImageFit, Builder, State, Menu, Color, Stack, Text } from '@kit.ArkUI';
import { UIContext } from '@ohos.arkui.UIContext';
import { MenuItem, Resource, WebElementType, WebResponseType, MenuType, WebContextMenuResult } from '@kit.ArkUI';
import { MenuItemOptions, DrawableDescriptor, ImageContent, PixelMap, HitTestMode } from '@kit.ArkUI';
import { OnContextMenuShowEvent, $$, TextAlign, CopyOptions, Progress, Alignment, TextOverflow, ProgressType } from '@kit.ArkUI';
import pasteboard from '@ohos.pasteboard';

interface PreviewBuilderParam {
  width: number;
  height: number;
  url:Resource | string;
}

interface PreviewBuilderParamForImage {
  previewImage: PixelMap | DrawableDescriptor | ImageContent | String | Resource;
  width: number;
  height: number;
}

@Entry
@Component
struct SelectionMenuLongPress {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  previewController: webview.WebviewController = new webview.WebviewController(undefined);
  @Builder PreviewBuilder($$: PreviewBuilderParam){
    Column() {
      Stack(){
        Text("") // 可选择是否展示url
          .padding(5)
          .width('100%')
          .textAlign(TextAlign.Start)
          .backgroundColor(Color.White)
          .copyOption(CopyOptions.LocalDevice)
          .maxLines(1)
          .textOverflow({overflow:TextOverflow.Ellipsis})
          Progress({ value: this.progressValue, total: 100, type: ProgressType.Linear }) // 展示进度条
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
        .hitTestBehavior(HitTestMode.None) // 使预览Web不响应手势
    }.width($$.width).height($$.height) // 设置预览宽高
  }

  private result: WebContextMenuResult | undefined = undefined;
  @State previewImage: PixelMap | DrawableDescriptor | ImageContent | String | Resource = '';
  @State previewWidth: number = 1;
  @State previewHeight: number = 1;
  @State previewWidthImage: number = 1;
  @State previewHeightImage: number = 1;
  @State linkURL:string = "";
  @State progressValue:number = 0;
  @State progressVisible:boolean = true;
  uiContext: UIContext = this.getUIContext();

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

  @Builder PreviewBuilderGlobalForImage($$: PreviewBuilderParamForImage) {
    Column() {
      Image($$.previewImage)
        .objectFit(ImageFit.Fill)
        .autoResize(true)
    }.width($$.width).height($$.height)
  }

  @Builder
  LinkMenuBuilder() {
    Menu() {
      MenuItem({ content: '复制链接', } as MenuItemOptions)
        .onClick(() => {
          const pasteboardData = pasteboard.createData(pasteboard.MIMETYPE_TEXT_PLAIN, this.linkURL);
          const systemPasteboard = pasteboard.getSystemPasteboard();
          systemPasteboard.setData(pasteboardData);
        })
      MenuItem({content:'打开链接'} as MenuItemOptions)
        .onClick(()=>{
          this.controller.loadUrl(this.linkURL);
        })
    }
  }
  @Builder
  ImageMenuBuilder() {
    Menu() {
      MenuItem({ content: '复制图片', } as MenuItemOptions)
        .onClick(() => {
          this.result?.copyImage();
          this.result?.closeContextMenu();
        })
    }
  }
  @Builder
  TextMenuBuilder() {
    Menu() {
      MenuItem({ content: '复制', } as MenuItemOptions)
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
            preview: () => {
              this.PreviewBuilder({
                width: 500,
                height: 400,
                url: this.linkURL
              })
            },
            menuType: MenuType.PREVIEW_MENU
          })
        .bindSelectionMenu(WebElementType.IMAGE, this.ImageMenuBuilder, WebResponseType.LONG_PRESS,
          {
            onAppear: () => {},
            onDisappear: () => {
              this.result?.closeContextMenu();
            },
            preview: () => {
              this.PreviewBuilderGlobalForImage({
                previewImage: this.previewImage,
                width: this.previewWidthImage,
                height: this.previewHeightImage,
              })
            },
            menuType: MenuType.PREVIEW_MENU
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
            // 返回true表示拦截系统默认的上下文菜单，使用自定义菜单
            return true;
          }
          return false;
        })
    }

  }
  // 侧滑返回
  onBackPress(): boolean {
    if (this.controller.accessStep(-1)) {
      this.controller.backward();
      return true;
    } else {
      return false;
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>长按复制文本</title>
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
        <!--img.png为html同目录下图片-->
        <img src="img.png">
    </div>

    <div class="context">
        <a  href="https://www.example.com">长按链接唤起菜单</a>
    </div>

    <div class="context">
        <span>在这个数字时代，文本复制功能变得日益重要。无论是引用名言、保存重要信息，还是分享有趣的内容，复制文本都是我们日常操作的一部分。</span>
    </div>

</div>
<br>

<script>
    function copySelectedText() {
        const selectedText = window.getSelection().toString();
        if (selectedText.length > 0) {
            // 使用Clipboard API复制文本
            navigator.clipboard.writeText(selectedText)
                .then(() => {
                    showNotification();
                })
                .catch(err => {
                    console.error('复制失败:', err);
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
default blankScreenDetectionConfig(detectConfig: BlankScreenDetectionConfig | undefined): this
```

The options for blank screen detection.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| detectConfig | [BlankScreenDetectionConfig](arkts-arkweb-web-blankscreendetectionconfig-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// onDetectedBlankScreen.ets
import { webview } from '@kit.ArkWeb';
import { Entry, Text, Column, Component, Web, BlankScreenDetectionEventInfo,BlankScreenDetectionMethod } from '@ohos.arkui.component'
import { State } from '@ohos.arkui.stateManagement'
import web_webview from '@ohos.web.webview';
@Entry
@Component
struct WebComponent {
  controller: web_webview.WebviewController = new web_webview.WebviewController(undefined);

  build() {
    Column() {

      Web({ src: "https://www.example.com/", controller: this.controller })
        .onDetectedBlankScreen((event: BlankScreenDetectionEventInfo | undefined) =>{
          if (event) {
            console.info(`Found blank screen on ${event.url}.`);
            console.info(`Found blank screen reason is ${event.blankScreenReason}.`);
            console.info(`Found blank screen blankScreenDetails is ${event.blankScreenDetails?.detectedContentfulNodesCount}.`);
          }
        })
        .blankScreenDetectionConfig({
          enable:true,
          detectionTiming:[2,4,6,8],
          detectionMethods:[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN],
          contentfulNodesCountThreshold:17
        })
    }
  }
}
```

## blockNetwork

```TypeScript
default blockNetwork(block: boolean | undefined): this
```

Whether web component can load resource from network.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| block | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, State } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default blurOnKeyboardHideMode(mode: BlurOnKeyboardHideMode | undefined): this
```

Sets the blur on for elements on webview when soft keyboard is hidden manually.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [BlurOnKeyboardHideMode](arkts-arkweb-web-bluronkeyboardhidemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, BlurOnKeyboardHideMode, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State blurMode: BlurOnKeyboardHideMode = BlurOnKeyboardHideMode.BLUR;

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .blurOnKeyboardHideMode(this.blurMode)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>测试网页</title>
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
default bypassVsyncCondition(condition: WebBypassVsyncCondition | undefined): this
```

Set up a condition that bypass vsync If the condition is matched, the drawing schedule does not reply on Vsync scheduling and directly rendering and drawing

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| condition | [WebBypassVsyncCondition](arkts-arkweb-web-webbypassvsynccondition-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Web, Button, Column, Component, Entry, WebBypassVsyncCondition } from '@ohos.arkui.component';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default cacheMode(cacheMode: CacheMode | undefined): this
```

Sets the mode of cache in Web.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cacheMode](#cachemode) | [CacheMode](arkts-arkweb-web-cachemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, State, CacheMode } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State mode: CacheMode = CacheMode.NONE;

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
default copyOptions(value: CopyOptions | undefined): this
```

Called to set copy option

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CopyOptions](../../apis-arkui/arkts-apis/arkts-arkui-copyoptions-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
  'use static'
  import { Web, Column, Component, Entry, CopyOptions } from '@kit.ArkUI';
  import { webview } from '@kit.ArkWeb';

  @Entry
  @Component
  struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default darkMode(mode: WebDarkMode | undefined): this
```

Sets the web dark mode. By default, web dark mode is disabled. When it is enabled, the Web component enables the dark theme defined for web pages if the theme has been defined in prefers-color-scheme of a media query, and remains unchanged otherwise. To enable the forcible dark mode, use this API with forceDarkAccess.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WebDarkMode](arkts-arkweb-web-webdarkmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State, WebDarkMode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
@State mode: WebDarkMode = WebDarkMode.ON;

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
default databaseAccess(databaseAccess: boolean | undefined): this
```

Sets whether to enable database access. By default, this feature is disabled.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [databaseAccess](#databaseaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default dataDetectorConfig(config: TextDataDetectorConfig | undefined): this
```

Data detector with config.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [TextDataDetectorConfig](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-textdatadetectorconfig-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import {
  Entry,
  Component,
  Column,
  Web,
  $rawfile,
  TextDataDetectorType,
  TextDecorationType,
  TextDecorationStyle,
  Color
} from '@ohos.arkui.component'
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>dataDetectorConfig示例</title>
</head>
<body>
    <p> 电话：400-123-4567 </p>
    <p> 邮箱：12345678901@example.com </p>
    <p> 网址：www.example.com（此项不识别）</p>
</body>
</html>
```

## defaultFixedFontSize

```TypeScript
default defaultFixedFontSize(size: int | undefined): this
```

Sets the default font size for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
@State fontSize: Int = 16;

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
default defaultFontSize(size: int | undefined): this
```

Sets the default font size for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
@State fontSize: Int = 13;

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
default defaultTextEncodingFormat(textEncodingFormat: string | undefined): this
```

Set the default text encodingFormat value of webview. The default value is UTF-8.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| textEncodingFormat | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
        // 设置高
        .height(500)
        .defaultTextEncodingFormat("UTF-8")
        .javaScriptAccess(true)
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

build() {
  Column() {
    Web({ src: $rawfile('index.html'), controller: this.controller })
    // 设置高
      .height(500)
      .defaultTextEncodingFormat("UTF-8")
      .javaScriptAccess(true)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width" />
    <title>My test html5 page</title>
</head>
<body>
    <p>hello world, 你好世界!</p>
</body>
</html>
```

## domStorageAccess

```TypeScript
default domStorageAccess(domStorageAccess: boolean | undefined): this
```

Sets whether to enable the DOM Storage API. By default, this feature is disabled.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [domStorageAccess](#domstorageaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default editMenuOptions(editMenu: EditMenuOptions | undefined): this
```

Set the custom text menu.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| editMenu | [EditMenuOptions](../../apis-arkui/arkts-apis/arkts-arkui-textcommon-editmenuoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
      // 过滤用户需要的系统按键
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
    items.push(customItem1);// 在选项列表后添加新选项
    items.unshift(customItem2);// 在选项列表前添加选项

    return items;
  }

  onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
    if (menuItem.id.equals(TextMenuItemId.CUT)) {
      // 用户自定义行为
      console.info("拦截 id：CUT")
      // 返回true表示拦截此菜单项，不执行系统默认的剪切操作
      return true;
    } else if (menuItem.id.equals(TextMenuItemId.COPY)) {
      // 用户自定义行为
      console.info("不拦截 id：COPY")
      // 返回false表示不拦截此菜单项，执行系统默认的复制操作
      return false;
    } else if (menuItem.id.equals(TextMenuItemId.of('customItem1'))) {
      // 用户自定义行为
      console.info("拦截 id：customItem1")
      return true;// 用户自定义菜单选项返回true时点击后不关闭菜单，返回false时关闭菜单
    } else if (menuItem.id.equals((TextMenuItemId.of($r('app.string.customItem2'))))){
      // 用户自定义行为
      console.info("拦截 id：app.string.customItem2")
      return true;
    }
    return false;// 返回默认值false
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
    menuItems.push(item1);// 在选项列表后添加新选项
    menuItems.unshift(item2);// 在选项列表前添加选项

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, State, Menu, $r } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { MenuItem, TextMenuItem, TextMenuItemId, TextRange, EditMenuOptions } from '@kit.ArkUI';

let selectText: string = '';
class TestClass {
  setSelectText(param: String) {
    selectText = param.toString();
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State testObj: TestClass = new TestClass();

  onCreateMenu(menuItems: Array<TextMenuItem>): Array<TextMenuItem> {
    let items = menuItems.filter((menuItem) => {
      // 过滤用户需要的系统按键。
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
    items.push(customItem1); // 在选项列表后添加新选项。
    items.unshift(customItem2); // 在选项列表前添加选项。

    return items;
  }

  onMenuItemClick(menuItem: TextMenuItem, textRange: TextRange): boolean {
    if (menuItem.id.equals(TextMenuItemId.CUT)) {
      // 用户自定义行为。
      console.info("拦截 id：CUT")
      // 返回true表示拦截此菜单项，不执行系统默认的剪切操作
      return true;
    } else if (menuItem.id.equals(TextMenuItemId.COPY)) {
      // 用户自定义行为。
      console.info("不拦截 id：COPY")
      // 返回false表示不拦截此菜单项，执行系统默认的复制操作
      return false;
    } else if (menuItem.id.equals(TextMenuItemId.of('customItem1'))) {
      // 用户自定义行为。
      console.info("拦截 id：customItem1")
      return true; // 用户自定义菜单选项返回true时点击后不关闭菜单，返回false时关闭菜单。
    } else if (menuItem.id.equals(TextMenuItemId.of('customItem2'))) {
      // 用户自定义行为。
      console.info("拦截 id：app.string.customItem2")
      return true;
    }
    return false; // 返回默认值false。
  }

  @State EditMenuOptions: EditMenuOptions = {
    onCreateMenu: (items: Array<TextMenuItem>) => this.onCreateMenu(items),
    onMenuItemClick: (item: TextMenuItem, range: TextRange) => this.onMenuItemClick(item, range),
  } as EditMenuOptions;

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .editMenuOptions(this.EditMenuOptions)
        .javaScriptProxy({
          jsObject: this.testObj,
          name: "testObjName",
          methodList: ["setSelectText"],
          controller: this.controller,
        })
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>测试网页</title>
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
default enableAutoFill(value: boolean | undefined): this
```

Sets whether enable auto fill or not.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Column, Component, Web, $rawfile } from '@ohos.arkui.component'
import web_webview from '@ohos.web.webview';

@Entry
@Component
struct WebComponent {
  controller: web_webview.WebviewController = new web_webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableAutoFill(true)

    }
  }
}
```

加载的html文件：

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0;" name="viewport"/>
    <title>自动填充测试</title>
  </head>
  <body>
    <h4 align="center">自动填充测试</h4>
    <form method="post" action="">
      <div align="center">
        <label for="name" style="width: 120px; display: inline-block; text-align: end;">姓名:</label>
        <input type="text" id="name" autocomplete="name"/><br/><br/>
        <label for="tel-national" style="width: 120px; display: inline-block; text-align: end;">手机号:</label>
        <input type="text" id="tel-national" autocomplete="tel-national"/><br/><br/>
      </div>
      <div align="center">
        <button type="submit" style="width: 80px">提交</button>
      </div>
    </form>
  </body>
</html>
```

## enableDataDetector

```TypeScript
default enableDataDetector(enable: boolean | undefined): this
```

Enable data detector.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import { Entry, Component, Column, Web, $rawfile } from '@ohos.arkui.component'
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableDataDetector(true)
    }
  }
}
```

加载的html文件

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>enableDataDetector示例</title>
</head>
<body>
    <p> 电话：400-123-4567 </p>
    <p> 邮箱：example@example.com </p>
</body>
</html>
```

## enableDefaultContextMenu

```TypeScript
default enableDefaultContextMenu(enable: boolean | undefined): this
```

Set whether to enable the default right-click context menu.

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

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
default enableDrag(value: boolean | undefined): this
```

Enables or disables dragging for this component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

## enableFollowSystemFontWeight

```TypeScript
default enableFollowSystemFontWeight(follow: boolean | undefined): this
```

Sets whether to follow the system font weight.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| follow | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  build() {
    Column() {
      Web({ src: "www.example.com", controller: this.controller })
        .enableFollowSystemFontWeight(true)
    }
  }
}
```

## enableHapticFeedback

```TypeScript
default enableHapticFeedback(enabled: boolean | undefined): this
```

Enable or disable haptic feedback.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Permissions need to be configured: ohos.permission.VIBRATE. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableHapticFeedback(true)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
  <head>
      <title>测试网页</title>
  </head>
  <body>
    <h1>enableHapticFeedback Demo</h1>
    <span>enable haptic feedback</span>
  </body>
</html>
```

## enableImageAnalyzer

```TypeScript
default enableImageAnalyzer(enable: boolean | undefined): this
```

Set up web component to support AI image recognition capability.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
        .enableImageAnalyzer(true) // 如果需要关闭图片分析能力，需要显式设置为false
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import { Entry, Component, Column, Web, $rawfile } from '@ohos.arkui.component'
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableImageAnalyzer(true) // 如果需要关闭图片分析能力，需要显式设置为false
    }
  }
}
```

加载的html文件：

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
    <!--example.jpg为html同目录下图片-->
    <img src="example.jpg" alt="待AI分析的图片">
  </div>
</body>
</html>
```

## enableNativeEmbedMode

```TypeScript
default enableNativeEmbedMode(enabled: boolean | undefined): this
```

Sets whether to enable the same-layer rendering feature.<p>&lt;strong&gt;API Note&lt;/strong&gt;: &lt;strong&gt;Performance Note&lt;/strong&gt;: <p>For details about how to rendering native components on the Web using same-layer rendering. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default enableNativeMediaPlayer(config: NativeMediaPlayerConfig | undefined): this
```

开启[应用接管网页媒体播放功能](../../../web/app-takeovers-web-media.md)。当属性没有显式调用时，默认不开启接管网页媒体播放功能。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [NativeMediaPlayerConfig](arkts-arkweb-web-nativemediaplayerconfig-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .enableNativeMediaPlayer({ enable: true, shouldOverlay: false })
    }
  }
}
```

## enableScrollDirectionalLock

```TypeScript
default enableScrollDirectionalLock(value: boolean | undefined, type: ScrollDirectionalLockType | undefined): this
```

Enables or disables directional lock for scroll gestures in the WebView component.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |
| type | [ScrollDirectionalLockType](arkts-arkweb-web-scrolldirectionallocktype-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
        // 在所有场景下支持滑动方向的锁定
        .enableScrollDirectionalLock(true, ScrollDirectionalLockType.ALL)
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, $rawfile, ScrollDirectionalLockType } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .width('100%')
        .height('100%')
        // 在所有场景下支持滑动方向的锁定
        .enableScrollDirectionalLock(true, ScrollDirectionalLockType.ALL)
    }
  }
}
```

加载的html文件。

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

## enableSelectedDataDetector

```TypeScript
default enableSelectedDataDetector(enable: boolean | undefined): this
```

Enable selected data detector.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// enableSelectedDataDetector.ets
'use static'
import { Web, Column, Component, Entry, $rawfile} from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableSelectedDataDetector(true)
    }
  }
}
```

加载的html文件

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>enableSelectedDataDetector示例</title>
</head>
<body>
    <p> 电话：400-123-4567 </p>
    <p> 邮箱：example@example.com </p>
</body>
</html>
```

## enableWebAVSession

```TypeScript
default enableWebAVSession(enabled: boolean | undefined): this
```

设置是否支持应用对接到播控中心。当属性没有显式设置时，默认支持应用对接到播控中心。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .enableWebAVSession(true)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>视频播放页面</title>
</head>
<body>
    <h1>视频播放</h1>
    <video id="testVideo" controls>
        <!--在resources的rawfile目录中放置任意一个mp4媒体文件，并将其命名为example.mp4-->
        <source src="example.mp4" type="video/mp4">
    </video>
</body>
</html>
```

## fileAccess

```TypeScript
default fileAccess(fileAccess: boolean | undefined): this
```

Sets whether to enable access to the file system in the application. This setting dose not affect the access to the files specified though \$rawfile(filepath/filename). <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> fileAccess is disabled by default since API version 12. When fileAccess is set to false, files in the read-only /data/storage/el1/bundle/entry/resources/resfile<br> directory can still be accessed through the file protocol. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [fileAccess](#fileaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default forceDarkAccess(access: boolean | undefined): this
```

Sets whether to enable forcible dark mode for the web page. This API is applicable only when dark mode is enabled in [darkMode](#darkmode).

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| access | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State, WebDarkMode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
@State mode: WebDarkMode = WebDarkMode.ON;
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
default forceDisplayScrollBar(enabled: boolean | undefined): this
```

Set whether the scroll bar is permanent. In the resident state, when the page size exceeds one page, the scroll bar appears and does not disappear.Scroll bar resident is not supported in full expansion mode, that is, when layoutMode is WebLayoutMode.FIT_CONTENT mode, the parameter enabled is false.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

加载的html文件。

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
default forceEnableZoom(enable: boolean | undefined): this
```

Set whether to comply with the zoom restrictions set by the&lt;meta name="viewport"&gt;tag in the webpage.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Column, Component, Web } from '@ohos.arkui.component'
import webview from '@ohos.web.webview';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'resource://rawfile/index.html', controller: this.controller })
        .forceEnableZoom(true)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
  <title>测试网页</title>
</head>
<body>
  <h1>forceEnableZoom Demo</h1>
  <span>You can scale page when forceEnableZoom is true.</span>
</body>
</html>
```

## geolocationAccess

```TypeScript
default geolocationAccess(geolocationAccess: boolean | undefined): this
```

Set whether to enable geolocation access. By default, this feature is enabled. For details, see Managing Location Permissions.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [geolocationAccess](#geolocationaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default gestureFocusMode(mode: GestureFocusMode | undefined): this
```

Set the gesture focus acquisition mode. When users interact with the web using different gestures, this determines whether and when focus is acquired based on the configured mode. Default value: DEFAULT, where all gestures acquire focus on touch down.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [GestureFocusMode](arkts-arkweb-web-gesturefocusmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-sta示例：

```TypeScript
// xxx.ets
'use static'

import { Entry, Component, Web, Column, State, GestureFocusMode, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State mode: GestureFocusMode = GestureFocusMode.DEFAULT;
  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .gestureFocusMode(this.mode)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>测试网页</title>
</head>
<body>
  <input type="text" placeholder="Text">
</body>
</html>
```

## horizontalScrollBarAccess

```TypeScript
default horizontalScrollBarAccess(horizontalScrollBar: boolean | undefined): this
```

Set whether paint horizontal scroll bar.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> After controlling the horizontal scrollbar's visibility through the @State variable, you need to call controller.refresh() to take effect.<br> When frequently changing the @State variable dynamically, it is recommended to match the toggle variable with the Web component one-to-one. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| horizontalScrollBar | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State isShow: boolean = true;
  @State btnMsg: string = '隐藏滚动条';

  build() {
    Column() {
      // 通过@State变量改变横向滚动条的隐藏/显示后，需调用this.controller.refresh()后生效
      Button('refresh')
        .onClick(() => {
          if (this.isShow) {
            this.isShow = false;
            this.btnMsg = '显示滚动条';
          } else {
            this.isShow = true;
            this.btnMsg = '隐藏滚动条';
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, State, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State isShow: boolean = true;
  @State btnMsg: string = '隐藏滚动条';

  build() {
    Column() {
      // 通过@State变量改变横向滚动条的隐藏/显示后，需调用this.controller.refresh()后生效。
      Button('refresh')
        .onClick(() => {
          if (this.isShow) {
            this.isShow = false;
            this.btnMsg = '隐藏滚动条';
          } else {
            this.isShow = true;
            this.btnMsg = '显示滚动条';
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

加载的html文件。

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
default imageAccess(imageAccess: boolean | undefined): this
```

设置是否允许自动加载图片资源。当属性没有显式调用时，允许自动加载图片资源。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [imageAccess](#imageaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default initialScale(percent: double | undefined): this
```

Sets the initial scale for the Web.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| percent | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'

import { Web, Column, Component, Entry, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State percent: double = 100;

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
default javaScriptAccess(javaScriptAccess: boolean | undefined): this
```

Sets whether the Web allows JavaScript scripts to execute.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [javaScriptAccess](#javascriptaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
  'use static'
  import { webview } from '@kit.ArkWeb';
  import { Entry, Column, Component, Web } from '@kit.ArkUI';

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default javaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this
```

Injects the JavaScripts script into the Web component. When the specified page or document has been loaded, the script is executed on any page whose source matches scriptRules. <p>&lt;strong&gt;API NOTE&lt;/strong&gt;:<br> The script runs after any JavaScript code of the page, when the DOM tree has been loaded and rendered. The script is excuted in the lexicographic order, not array order. If the array order is required, you are advised to use the runJavaScriptOnDocumentEnd interface. You are not advised to use this API together with runJavaScriptOnDocumentEnd. When scripts with identical content are injected multiple times, silent deduplication will be performed: repeated scripts will neither be displayed nor prompted, and the scriptRules used during the first injection will be adopted. <p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-web-scriptitem-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, State, ScriptItem, $rawfile, Color } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  private jsStr: string =
    "window.document.getElementById(\"result\").innerHTML = 'this is msg from javaScriptOnDocumentEnd'";
  @State scripts: Array<ScriptItem> = [
    { script: this.jsStr, scriptRules: ["*"] }
  ] as ScriptItem[];

  build() {
    Column() {
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
default javaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this
```

Injects the JavaScripts script into the Web component. When the specified page or document starts to be loaded, the script is executed on any page whose source matches scriptRules. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> The script runs before any JavaScript code of the page, when the DOM tree may not have been loaded or rendered. The script is executed in the lexicographic order, not array order. If the array order is required, you are advised to use the runJavaScriptOnDocumentStart interface. You are not advised to use this API together with runJavaScriptOnDocumentStart. When scripts with identical content are injected multiple times, silent deduplication will be performed: repeated scripts will neither be displayed nor prompted, and the scriptRules used during the first injection will be adopted. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-web-scriptitem-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

## javaScriptProxy

```TypeScript
default javaScriptProxy(javaScriptProxy: JavaScriptProxy | undefined): this
```

Registers the supplied ArkTS object in javaScriptProxy into this Web component. The object is registered into all frames of the web page, including all frames, using the specified name in javaScriptProxy. This allows the methods of the ArkTS object in javaScriptProxy to be accessed from JavaScript.<p>&lt;strong&gt;API Note&lt;/strong&gt;: &lt;strong&gt;Performance Note&lt;/strong&gt;: <p>For details about how to arkWeb rendering framework adaptation solution, see [ArkWeb Rendering Framework Adaptation] com/consumer/en/doc/best-practices/bpta-arkweb_rendering_framework </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [javaScriptProxy](#javascriptproxy) | [JavaScriptProxy](arkts-arkweb-web-javascriptproxy-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Text, Column, Component, Button, Web, JavaScriptProxy, WebKeyboardAvoidMode, State } from '@kit.ArkUI';
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

  testString(): void {
    console.info('toString' + "interface instead.");
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State testObj: TestObj = new TestObj();
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
          jsObject: this.testObj,
          name: "objName",
          methodList: ["test", "testString"],
          asyncMethodList: ["asyncTest"],
          controller: this.controller,
        } as JavaScriptProxy)
    }
  }
}
```

## keyboardAppearance

```TypeScript
default keyboardAppearance(mode: WebKeyboardAppearanceMode | undefined): this
```

Set the WebKeyboardAppearanceMode to determine the immersive mode for the soft keyboard.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WebKeyboardAppearanceMode](arkts-arkweb-web-webkeyboardappearancemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Web, $rawfile, WebKeyboardAppearanceMode } from '@ohos.arkui.component';
import { State } from '@ohos.arkui.stateManagement';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State appearanceMode: WebKeyboardAppearanceMode = WebKeyboardAppearanceMode.DARK_IMMERSIVE;

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
      .keyboardAppearance(this.appearanceMode)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>测试网页</title>
</head>
<body>
  <input type="text" placeholder="Text">
</body>
</html>
```

## keyboardAvoidMode

```TypeScript
default keyboardAvoidMode(mode: WebKeyboardAvoidMode | undefined): this
```

When the keyboard avoidance mode set by UIContext is [RESIZE](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-keyboardavoidmode-e.md#resize) mode, the interface function will not take effect.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WebKeyboardAvoidMode](arkts-arkweb-web-webkeyboardavoidmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, State, Column, Component, Entry, WebKeyboardAvoidMode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State avoidMode: WebKeyboardAvoidMode = WebKeyboardAvoidMode.RESIZE_VISUAL;

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .keyboardAvoidMode(this.avoidMode)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>测试网页</title>
</head>
<body>
  <input type="text" placeholder="Text">
</body>
</html>
```

## layoutMode

```TypeScript
default layoutMode(mode: WebLayoutMode | undefined): this
```

Sets the web layout mode.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Currently, only two web layout modes are supported: WebLayoutMode.NONE and WebLayoutMode.FIT_CONTENT. The following restrictions apply with the usage of WebLayoutMode.FIT_CONTENT: - If the Web component is wider or longer than 7680 px, specify the RenderMode.SYNC_RENDER mode when creating the Web component; otherwise, the screen may be blank. - After the Web component is created, dynamic switching of the layoutMode is not supported. - The width and height of a Web component cannot exceed 500,000 px when the RenderMode.SYNC_RENDER mode is specified, and cannot exceed 7680 px when the RenderMode.ASYNC_RENDER mode is specified. - Frequent changes to the page width and height will trigger a re-layout of the Web component, which can affect the user experience. - Waterfall web pages are not supported (drop down to the bottom to load more). - Only height adaptation is supported. Width adaptation is not supported. - Because the height is adaptive to the web page height, the component height cannot be changed by modifying the component height attribute. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [WebLayoutMode](arkts-arkweb-web-weblayoutmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, WebLayoutMode, RenderMode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
mode: WebLayoutMode = WebLayoutMode.FIT_CONTENT;

build() {
  Column() {
    Web({ src: 'www.example.com', controller: this.controller, renderMode: RenderMode.SYNC_RENDER })
      .layoutMode(this.mode)
    }
  }
}
```

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { State,Entry, Component, Web, Column, WebLayoutMode, RenderMode, OverScrollMode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default mediaOptions(options: WebMediaOptions | undefined): this
```

设置Web媒体播放的策略，其中包括：Web中的音频在重新获焦后能够自动续播的有效期、应用内多个Web实例的音频是否独占。当该属性未显式设置时，默认Web中的音频重新获焦后无法自动续播、应用内多个Web实例的音频是独占的。

> **说明：**&gt;
> - 同一Web实例中的多个音频均视为同一音频。&gt;
> - 该媒体播放策略将同时管控有声视频。&gt;
> - 建议为所有Web组件设置相同的[audioExclusive](../arkts-components/arkts-arkweb-webmediaoptions-i.md)值。&gt;
> - 音视频互相打断在应用内和应用间生效，续播只在应用间生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [WebMediaOptions](arkts-arkweb-web-webmediaoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, State, WebMediaOptions, AudioSessionType } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State options: WebMediaOptions =
    { resumeInterval: 10, audioExclusive: true, audioSessionType: AudioSessionType.AMBIENT } as WebMediaOptions;

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
default mediaPlayGestureAccess(access: boolean | undefined): this
```

设置有声视频的自动播放是否需要用户手动点击，静音视频播放不受该接口管控。当该属性未显式设置时，默认有声视频的自动播放需要用户手动点击。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| access | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .mediaPlayGestureAccess(true)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>视频播放页面</title>
</head>
<body>
<h1>视频播放</h1>
<video id="testVideo" controls autoplay>
    // 需要在video标签中配置autoplay属性，允许视频自动播放
    // 在resources的rawfile目录放置任意一个mp4媒体文件，并将其命名为example.mp4
    <source src="example.mp4" type="video/mp4">
</video>
</body>
</html>
```

## metaViewport

```TypeScript
default metaViewport(enabled: boolean | undefined): this
```

Sets whether the viewport property of the meta tag is enabled.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> If the device is 2-in-1, the viewport property is not supported. This means that, regardless of whether this parameter is set to true or false, the viewport property will not be parsed and a default layout will be used.<br> If the device is a tablet, the viewport-fit property of the meta tag is parsed regardless of whether this parameter is set to true or false. When viewport-fit is set to cover, the size of the safe area can be obtained through the CSS attribute.<br> The viewport parameter of the meta tag on the frontend HTML page is enabled or disabled based on whether User-Agent contains the Mobile field. If a User-Agent does not contain the Mobile field, the viewport property in the meta tag is disabled by default. In this case, you can explicitly set the metaViewport property to true to overwrite the disabled state. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

build() {
  Column() {
    Web({ src: $rawfile('index.html'), controller: this.controller })
      .metaViewport(true)
    }
  }
}
```

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <p>hello world, 你好世界!</p>
</body>
</html>
```

## minFontSize

```TypeScript
default minFontSize(size: int | undefined): this
```

Sets the minimum font size for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
@State fontSize: Int = 13;

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
default minLogicalFontSize(size: int | undefined): this
```

Sets the minimum logical font size for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { State, Entry, Column, Component, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State fontSize: Int = 13;

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
default mixedMode(mixedMode: MixedMode | undefined): this
```

Sets the behavior when a secure origin attempts to load a resource from an insecure origin. The default is MixedMode.None, meaning not allow a secure origin to load content from an insecure origin.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [mixedMode](#mixedmode) | [MixedMode](arkts-arkweb-web-mixedmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, State, MixedMode } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State mode: MixedMode = MixedMode.ALL;
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
default multiWindowAccess(multiWindow: boolean | undefined): this
```

Set whether multiple windows are supported. When multiple windows permissions are enabled, the [onWindowNew](#onwindownew) event needs to be implemented.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| multiWindow | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

## nativeEmbedOptions

```TypeScript
default nativeEmbedOptions(options?: EmbedOptions | undefined): this
```

Sets the embed options, only valid when enableNativeEmbedMode is true.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [EmbedOptions](arkts-arkweb-web-embedoptions-i.md) \| undefined | 否 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile,Entry, Component, Web, Column, EmbedOptions } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
options: EmbedOptions = {supportDefaultIntrinsicSize: true} as EmbedOptions;

build() {
  Column() {
    Web({ src: $rawfile("index.html"), controller: this.controller })
      .enableNativeEmbedMode(true)
      .nativeEmbedOptions(this.options)
    }
  }
}
```

加载的html文件

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>同层渲染固定大小测试html</title>
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
default nestedScroll(value: NestedScrollOptions | NestedScrollOptionsExt | undefined): this
```

Called to setting the nested scroll options.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> You can set four directions: up, down, left, and right, or set nested scrolling modes for forward and backward directions to achieve scrolling linkage with the parent component.<br> When value is of type NestedScrollOptionsExt (four directions: up, down, left, and right), the default scrolling options for scrollUp, scrollDown, scrollLeft, and scrollRight are NestedScrollMode.SELF_FIRST.<br> When value is of type NestedScrollOptions (two directions: forward and backward), the default scrolling options for scrollForward and scrollBackward are NestedScrollMode.SELF_FIRST.<br> Supported nested scrolling containers: Grid, List, Scroll, Swiper, Tabs, WaterFlow, Refresh, bindSheet.<br> Supported nested scrolling input events: gestures, mouse, and trackpad.<br> In nested scrolling scenarios, since web scrolling to the edge will prioritize triggering the overscroll bounce effect, it is recommended to set overScrollMode to OverScrollMode.NEVER to avoid affecting the user experience in this scenario. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [NestedScrollOptions](../../apis-arkui/arkts-components/arkts-arkui-nestedscrolloptions-i.md) \| [NestedScrollOptionsExt](arkts-arkweb-web-nestedscrolloptionsext-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, NestedScrollMode, NestedScrollOptions } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .nestedScroll({
          scrollForward: NestedScrollMode.SELF_FIRST,
          scrollBackward: NestedScrollMode.SELF_FIRST
        } as NestedScrollOptions)
    }
  }
}
```

ArkTS-Dyn示例：

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
        Text("嵌套Web")
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, NestedScrollMode, Scroll, Text } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { NestedScrollOptionsExt, Color } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined)

  build() {
    Scroll() {
      Column() {
        Text("嵌套Web")
          .height("25%")
          .width("100%")
          .fontSize(30)
          .backgroundColor(Color.Yellow)
        Web({
          src: $rawfile('index.html'),
          controller: this.controller
        })
          .nestedScroll({
            scrollUp: NestedScrollMode.SELF_FIRST,
            scrollDown: NestedScrollMode.PARENT_FIRST,
            scrollLeft: NestedScrollMode.SELF_FIRST,
            scrollRight: NestedScrollMode.SELF_FIRST,
          } as NestedScrollOptionsExt)
      }
    }
  }
}
```

加载的html文件。

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
        text-align: center;       /* 水平居中 */
        line-height: 200px;       /* 垂直居中（值等于容器高度） */
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
default onActivateContent(callback: VoidCallback | undefined): this
```

Triggered when the web page is activated for window.open called by other web component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

// 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
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
          //该Web需要展示到前面，建议应用在这里进行tab或window切换的动作展示此web。
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
        // 需要使能multiWindowAccess。
        .multiWindowAccess(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController.close()
          }
          let popController: webview.WebviewController = new webview.WebviewController();
          // 将新窗口对应WebviewController返回给Web内核。
          // 若不调用event.handler.setWebController接口，会造成渲染进程阻塞。
          event.handler.setWebController(popController);
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController }),
            isModal: false
          })
          this.dialogController.open();
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { $rawfile, Component, Entry, Web, Column, CustomDialogController, CustomDialog } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

// 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
@CustomDialog
struct NewWebViewComp {
  controller?: CustomDialogController;
  webviewController1: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: "https://www.example.com", controller: this.webviewController1 })
        .javaScriptAccess(true)
        .multiWindowAccess(false)
        .onWindowExit(() => {
          if (this.controller) {
            this.controller?.close();
          }
        })
        .onActivateContent(() => {
          //该Web需要展示到前面，建议应用在这里进行tab或window切换的动作展示此web。
          console.info("NewWebViewComp onActivateContent")
        })
    }.height("50%")
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  dialogController: CustomDialogController | null = null;

  build() {
    Column() {
      Web({ src: $rawfile("window.html"), controller: this.controller })
        .javaScriptAccess(true)
        .allowWindowOpenMethod(true)
        // 需要使能multiWindowAccess。
        .multiWindowAccess(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController?.close()
          }
          let popController: webview.WebviewController = new webview.WebviewController(undefined);
          // 将新窗口对应WebviewController返回给Web内核。
          // 若不调用event.handler.setWebController接口，会造成渲染进程阻塞。
          event.handler.setWebController(popController);
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController }),
            isModal: false
          })
          this.dialogController?.open();
        })
    }
  }
}
```

```TypeScript
<!-- window.html页面代码 -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ActivateContentEvent</title>
</head>
<body>
<a href="#" onclick="openNewWindow('https://www.example.com')">打开新页面</a>
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
default onAdsBlocked(callback: OnAdsBlockedCallback | undefined): this
```

Called when received Ads blocked results. If blocked results exist at the end of page loading, the first call will be triggered. To avoid performance issues, subsequent results will be periodically reported through this api.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnAdsBlockedCallback](arkts-arkweb-onadsblockedcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Entry, Column, Component, Web, AdsBlockedDetails, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  @State totalAdsBlockCounts: number = 0;
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'https://www.example.com', controller: this.controller })
        .onAdsBlocked((details: AdsBlockedDetails) => {
          if (details) {
            console.info(' Blocked ' + details.adsBlocked.length + ' in ' + details.url);
            let adList: Array<string> = Array.from(details.adsBlocked);
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
default onAlert(callback: Callback<OnAlertEvent, boolean> | undefined): this
```

Triggered when the Web wants to display a JavaScript alert() dialog.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnAlertEvent](arkts-arkweb-web-onalertevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
            console.info('event.url:' + event.url);
            console.info('event.message:' + event.message);
            this.uiContext.showAlertDialog({
              title: 'onAlert',
              message: 'text',
              primaryButton: {
                value: 'ok',
                action: () => {
                  // 用户点击确认，调用handleConfirm通知Web组件确认结果
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, OnAlertEvent, AlertDialogParamWithConfirm } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onAlert((event: OnAlertEvent): boolean => {
          if (event) {
            console.info('event.url:' + event.url);
            console.info('event.message:' + event.message);

            this.uiContext.showAlertDialog({
              title: 'onAlert',
              message: event.message,
              confirm: {
                value: 'ok',
                action: () => {
                  // 用户点击确认，调用handleConfirm通知Web组件确认结果
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            } as AlertDialogParamWithConfirm);
          }
          return true;
        })
    }
  }
}
```

加载的html文件。

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
default onAudioStateChanged(callback: Callback<OnAudioStateChangedEvent> | undefined): this
```

设置网页上的音频播放状态发生改变时的回调函数。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnAudioStateChangedEvent](arkts-arkweb-web-onaudiostatechangedevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
          // 更新音频播放状态供后续使用
          this.playing = event.playing;
          console.info('onAudioStateChanged playing: ' + this.playing);
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { State, Web, Column, Component, Entry, OnAudioStateChangedEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct AudioPlayer {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State playing: boolean = false;

  build() {
    Column() {
       Web({ src: 'www.example.com', controller: this.controller })
        .onAudioStateChanged((event: OnAudioStateChangedEvent): void => {
          this.playing = event.playing;
          console.info('onAudioStateChanged playing: ' + this.playing);
        })
    }
  }
}
```

## onBeforeUnload

```TypeScript
default onBeforeUnload(callback: Callback<OnBeforeUnloadEvent, boolean> | undefined): this
```

Triggered when the Web wants to confirm navigation from JavaScript onbeforeunload.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnBeforeUnloadEvent](arkts-arkweb-web-onbeforeunloadevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, OnBeforeUnloadEvent, $rawfile } from '@kit.ArkUI';
import { UIContext, AlertDialogParamWithButtons } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onBeforeUnload((event: OnBeforeUnloadEvent): boolean => {
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
            } as AlertDialogParamWithButtons);
          }
          return true;
        })
    }
  }
}
```

加载的html文件。

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
default onCameraCaptureStateChange(callback: OnCameraCaptureStateChangeCallback | undefined): this
```

通知用户当前网页的摄像头状态，摄像头有三个状态，无状态（None），捕获中（Active），暂停中（Paused）。使用callback异步回调。可以通过startCamera，stopCamera，closeCamera这三个接口来切换摄像头的状态。这三个接口分别对应开启，暂停，停止摄像头功能。示例使用场景详见 [startCamera](../../../reference/apis-arkweb/arkts-apis-webview-WebviewController.md#startcamera)。

> **说明：**&gt;
> 当前网页正在使用摄像头时，返回在捕获中状态。&gt;
> 当前网页暂停使用摄像头时，返回暂停中状态。&gt;
> 当前网页完全没有使用摄像头时，返回无状态。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnCameraCaptureStateChangeCallback](arkts-arkweb-oncameracapturestatechangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, Button, OnPermissionRequestEvent, Context } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { UIContext } from "@kit.ArkUI";
import { AlertDialogParamWithButtons, AlertDialogButtonBaseOptions } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { PermissionRequestResult, common, abilityAccessCtrl } from '@kit.AbilityKit';
import { CameraCaptureStateChangeInfo } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA'],
      (err: BusinessError | null, data?: PermissionRequestResult) => {
        if (data) {
          console.info('data:' + JSON.stringify(data));
          console.info('data permissions:' + data.permissions);
          console.info('data authResults:' + data.authResults);
        }
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
        .onPermissionRequest((event: OnPermissionRequestEvent): void => {
          if (event) {
            const dialogOptions: AlertDialogParamWithButtons = {
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                },
              } as AlertDialogButtonBaseOptions,
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                },
              } as AlertDialogButtonBaseOptions,
              cancel: () => {
                event.request.deny();
              }
            };
            this.uiContext.showAlertDialog(dialogOptions);
          }
        })
        .onCameraCaptureStateChange((event: CameraCaptureStateChangeInfo | undefined): void => {
          if (event) {
            console.info("CameraCapture from ", event.originalState, " to ", event.newState);
          }
        })
    }
  }
}
```

加载的html文件

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
   <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()" />
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
default onClientAuthenticationRequest(callback: Callback<OnClientAuthenticationEvent> | undefined): this
```

Triggered when the Web page needs ssl client certificate from the user.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnClientAuthenticationEvent](arkts-arkweb-web-onclientauthenticationevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import { certificateManager } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
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

        // 注：badssl.com-client.p12需要替换为实际使用的证书文件
        let value: Uint8Array = this.context.resourceManager.getRawFileContentSync("badssl.com-client.p12");
        certificateManager.installPrivateCertificate(value, 'badssl.com', "1",
          async (err: BusinessError, data: certificateManager.CMResult) => {
            console.info(`installPrivateCertificate, uri==========${JSON.stringify(data.uri)}`)
            if (!err && data.uri) {
              this.uri = data.uri;
            }
          });
      })
      Button('加载需要客户端SSL证书的网站')
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

ArkTS-Dyn示例：

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

构造  对象以对接证书管理。

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
    // 注：com.example.myapplication需要写实际应用名称
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

    // 注：需要在MainAbility.ts文件的onCreate函数里添加GlobalContext.getContext().setObject("AbilityContext", this.context)
    let abilityContext = GlobalContext.getContext().getObject("AbilityContext") as common.UIAbilityContext;
    await abilityContext.startAbilityForResult(
      {
        bundleName: "com.ohos.certmanager",
        abilityName: "MainAbility",
        uri: "requestAuthorize",
        parameters: {
          appUid: this.appUid, // 传入申请应用的appUid
        }
      } as Want)
      .then((data: common.AbilityResult) => {
        if (!data.resultCode && data.want) {
          if (data.want.parameters) {
            this.authUri = data.want.parameters.authUri as string; // 授权成功后获取返回的authUri
          }
        }
      })
    return this.authUri;
  }
}
```

将当前Ability的上下文存储到GlobalContext中。

```TypeScript
// EntryAbility.ets
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { GlobalContext } from '../pages/GlobalContext';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      GlobalContext.getContext().setObject("AbilityContext", this.context);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
        return;
      }
      hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
```

实现双向认证功能。

```TypeScript
import { webview } from '@kit.ArkWeb';
import CertManagerService from './CertMgrService';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  certManager = CertManagerService.getInstance();

  aboutToAppear(): void {
    webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
  }

  build() {
    Column() {
      Button('加载需要客户端SSL证书的网站')
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
default onConfirm(callback: Callback<OnConfirmEvent, boolean> | undefined): this
```

Triggered when confirm() is invoked by the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnConfirmEvent](arkts-arkweb-web-onconfirmevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
            console.info('event.url:' + event.url);
            console.info('event.message:' + event.message);
            this.uiContext.showAlertDialog({
              title: 'onConfirm',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  // 用户点击取消，调用handleCancel通知Web组件取消结果
                  event.result.handleCancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  // 用户点击确认，调用handleConfirm通知Web组件确认结果
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, OnConfirmEvent, AlertDialogParamWithButtons } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { UIContext } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined)
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onConfirm((event: OnConfirmEvent): boolean => {
          if (event) {
            console.info('event.url:' + event.url);
            console.info('event.message:' + event.message);

            this.uiContext.showAlertDialog({
              title: 'onConfirm',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  // 用户点击取消，调用handleCancel通知Web组件取消结果
                  event.result.handleCancel();
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  // 用户点击确认，调用handleConfirm通知Web组件确认结果
                  event.result.handleConfirm();
                }
              },
              cancel: () => {
                event.result.handleCancel();
              }
            } as AlertDialogParamWithButtons)
          }
          return true;
        })
    }
  }
}
```

加载的html文件。

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
default onConsole(callback: Callback<OnConsoleEvent, boolean> | undefined): this
```

Triggered when the web page receives a JavaScript console message.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnConsoleEvent](arkts-arkweb-web-onconsoleevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
          }
          return false;
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, Button, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
          }
          return false;
        })
    }
  }
}
```

加载的html文件。

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
default onContextMenuHide(callback: OnContextMenuHideCallback | undefined): this
```

Triggered when called to allow custom hide of the context menu.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnContextMenuHideCallback](arkts-arkweb-oncontextmenuhidecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onContextMenuHide((): void => {
          console.info("onContextMenuHide callback");
        })
    }
  }
}
```

## onContextMenuShow

```TypeScript
default onContextMenuShow(callback: Callback<OnContextMenuShowEvent, boolean> | undefined): this
```

Triggered when called to allow custom display of the context menu.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnContextMenuShowEvent](arkts-arkweb-web-oncontextmenushowevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
  // 构建自定义菜单及触发功能接口
  MenuBuilder() {
    // 以垂直列表形式显示的菜单。
    Menu() {
      // 展示菜单Menu中具体的item菜单项。
      MenuItem({
        content: '撤销',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.undo();
          this.showMenu = false;
        })
      MenuItem({
        content: '重做',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.redo();
          this.showMenu = false;
        })
      MenuItem({
        content: '粘贴为纯文本',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.pasteAndMatchStyle();
          this.showMenu = false;
        })
      MenuItem({
        content: '复制图片',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copyImage();
          this.showMenu = false;
        })
      MenuItem({
        content: '保存图片',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.saveImage();
          this.showMenu = false;
        })
      MenuItem({
        content: '剪切',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.cut();
          this.showMenu = false;
        })
      MenuItem({
        content: '复制',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copy();
          this.showMenu = false;
        })
      MenuItem({
        content: '粘贴',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.paste();
          this.showMenu = false;
        })
      MenuItem({
        content: '复制链接',
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
        content: '全选',
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
        // 触发自定义弹窗
        .onContextMenuShow((event) => {
          if (event) {
            // 保存result供后续菜单操作使用
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

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import { Entry, Column, Component } from '@ohos.arkui.component'
import { State } from '@ohos.arkui.stateManagement'
import { $rawfile, Web, Builder, Menu, MenuItem, Placement, WebContextMenuResult } from '@ohos.arkui.component'
import { MenuItemOptions, CustomPopupOptions, PopupStateChangeParam } from '@ohos.arkui.component'
import { UIContext } from '@ohos.arkui.UIContext'
import { webview } from '@kit.ArkWeb';
import pasteboard from '@ohos.pasteboard';

const TAG = 'ContextMenu';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  private result: WebContextMenuResult | undefined = undefined;
  @State linkUrl: string = '';
  @State offsetX: number = 0;
  @State offsetY: number = 0;
  @State showMenu: boolean = false;
  uiContext: UIContext = this.getUIContext();

  @Builder
  // 构建自定义菜单及触发功能接口
  MenuBuilder() {
    // 以垂直列表形式显示的菜单。
    Menu() {
      // 展示菜单Menu中具体的item菜单项。
      MenuItem({
        content: '复制图片',
      } as MenuItemOptions)
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copyImage();
          this.showMenu = false;
        })
      MenuItem({
        content: '保存图片',
      })
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.saveImage();
          this.showMenu = false;
        })
      MenuItem({
        content: '剪切',
      } as MenuItemOptions)
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.cut();
          this.showMenu = false;
        })
      MenuItem({
        content: '复制',
      } as MenuItemOptions)
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.copy();
          this.showMenu = false;
        })
      MenuItem({
        content: '粘贴',
      } as MenuItemOptions)
        .width(100)
        .height(50)
        .onClick(() => {
          this.result?.paste();
          this.showMenu = false;
        })
      MenuItem({
        content: '复制链接',
      } as MenuItemOptions)
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
        content: '全选',
      } as MenuItemOptions)
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
      // 触发自定义弹窗
        .onContextMenuShow((event) => {
          if (event) {
            // 保存result供后续菜单操作使用
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
            builder: this.MenuBuilder,
            enableArrow: false,
            placement: Placement.LeftTop,
            offset: { x: this.offsetX, y: this.offsetY },
            mask: false,
            onStateChange: (e: PopupStateChangeParam) => {
              if (!e.isVisible) {
                this.showMenu = false;
                this.result!.closeContextMenu();
              }
            }
          } as CustomPopupOptions)
    }
  }
}
```

加载的html文件。

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<body>
  <h1>onContextMenuShow</h1>
  <a href="http://www.example.com" style="font-size:27px">链接www.example.com</a>
  <!-- rawfile下放任意一张图片命名为example.png -->
  <div><img src="example.png"></div>
  <p>选中文字鼠标右键弹出菜单</p>
</body>
</html>
```

## onControllerAttached

```TypeScript
default onControllerAttached(callback: (() => void) | undefined): this
```

The callback is triggered when the Controller is successfully bound to the Web component, and the Controller must be a WebviewController, and it is forbidden to call the interface related to the Web component before the event callback, otherwise a js-error exception will be thrown. Because the webpage has not been loaded when the callback is called, it is impossible to use interfaces related to operating webpages in the callback, such as [zoomIn](arkts-arkweb-webview-webviewcontroller-c.md#zoomin) and [zoomOut](arkts-arkweb-webview-webviewcontroller-c.md#zoomout), and you can use interfaces unrelated to operating webpages such as loadUrl and [getWebId](arkts-arkweb-webview-webviewcontroller-c.md#getwebid).

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Entry, Column, Component, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Entry, Column, Component, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件。

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
default onDataResubmitted(callback: Callback<OnDataResubmittedEvent> | undefined): this
```

Triggered when the form could be resubmitted.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnDataResubmittedEvent](arkts-arkweb-web-ondataresubmittedevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
      // 在网页中点击提交之后，点击refresh按钮可以重新提交时的触发函数。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, Button, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      // 在网页中点击提交之后，点击refresh按钮可以重新提交时的触发函数。
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

加载的html文件。

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
     <input type="submit" name="提交">
   </form>
 </body>
 </html>
```

## onDetectedBlankScreen

```TypeScript
default onDetectedBlankScreen(callback: OnDetectBlankScreenCallback | undefined): this
```

Triggered when web engine detects the current page is blank screen or nearly blank.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnDetectBlankScreenCallback](arkts-arkweb-ondetectblankscreencallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// onDetectedBlankScreen.ets
import { webview } from '@kit.ArkWeb';
import { Entry, Text, Column, Component, Web, BlankScreenDetectionEventInfo,BlankScreenDetectionMethod } from '@ohos.arkui.component'
import { State } from '@ohos.arkui.stateManagement'
import web_webview from '@ohos.web.webview';
@Entry
@Component
struct WebComponent {
  controller: web_webview.WebviewController = new web_webview.WebviewController(undefined);

  build() {
    Column() {

      Web({ src: "https://www.example.com/", controller: this.controller })
        .onDetectedBlankScreen((event: BlankScreenDetectionEventInfo | undefined) =>{
          if (event) {
            console.info(`Found blank screen on ${event.url}.`);
            console.info(`Found blank screen reason is ${event.blankScreenReason}.`);
            console.info(`Found blank screen blankScreenDetails is ${event.blankScreenDetails?.detectedContentfulNodesCount}.`);
          }
        })
        .blankScreenDetectionConfig({
          enable:true,
          detectionTiming:[2,4,6,8],
          detectionMethods:[BlankScreenDetectionMethod.DETECTION_CONTENTFUL_NODES_SEVENTEEN],
          contentfulNodesCountThreshold:17
        })
    }
  }
}
```

## onDownloadStart

```TypeScript
default onDownloadStart(callback: Callback<OnDownloadStartEvent> | undefined): this
```

Triggered when starting to download.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnDownloadStartEvent](arkts-arkweb-web-ondownloadstartevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, Button, $rawfile } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default onErrorReceive(callback: Callback<OnErrorReceiveEvent> | undefined): this
```

Triggered when the web page receives a web resource loading error.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnErrorReceiveEvent](arkts-arkweb-web-onerrorreceiveevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default onFaviconReceived(callback: Callback<OnFaviconReceivedEvent> | undefined): this
```

Triggered when the application receive a new favicon for the current web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnFaviconReceivedEvent](arkts-arkweb-web-onfaviconreceivedevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { image } from '@kit.ImageKit';
import { Web, Column, Component, Entry, OnFaviconReceivedEvent, State } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default onFirstContentfulPaint(callback: Callback<OnFirstContentfulPaintEvent> | undefined): this
```

Triggered when the first content rendering of web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnFirstContentfulPaintEvent](arkts-arkweb-web-onfirstcontentfulpaintevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column,OnFirstContentfulPaintEvent} from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

build() {
  Column() {
    Web({ src: 'www.example.com', controller: this.controller })
      .onFirstContentfulPaint((event:OnFirstContentfulPaintEvent):void => {
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
default onFirstMeaningfulPaint(callback: OnFirstMeaningfulPaintCallback | undefined): this
```

Triggered when the first meaningful paint occurs on the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnFirstMeaningfulPaintCallback](arkts-arkweb-onfirstmeaningfulpaintcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column,FirstMeaningfulPaint} from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

build() {
  Column() {
    Web({ src: 'www.example.com', controller: this.controller })
      .onFirstMeaningfulPaint((event:FirstMeaningfulPaint):void => {
        if(event) {
          console.info("onFirstMeaningfulPaint: [navigationStartTime]= " + event.navigationStartTime +
            ", [firstMeaningfulPaintTime]=" + event.firstMeaningfulPaintTime);
          }
        })
      }
    }
}
```

## onFirstScreenPaint

```TypeScript
default onFirstScreenPaint(callback: OnFirstScreenPaintCallback | undefined): this
```

Triggered after the first screen of the web page has been painted. The first screen contains the images, videos and texts in the viewport of the current navigation. The callback will not be triggered immediately when the first screen has been painted, but in a few seconds according to the current network condition. However, if the user scrolls or inputs before the first screen has been painted, the callback will be triggered immediately.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnFirstScreenPaintCallback](arkts-arkweb-onfirstscreenpaintcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// onFirstScreenPaint.ets
import { Column, Component, Entry, Web, FirstScreenPaint } from '@ohos.arkui.component'
import hilog from '@ohos.hilog'
import web_webview from '@ohos.web.webview';

@Entry
@Component
struct WebComponent {
  controller: web_webview.WebviewController = new web_webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'https://www.example.com/', controller: this.controller })
        .width('100%')
        .height('50%')
        .onFirstScreenPaint((event:FirstScreenPaint | undefined)=> {
          if (event) {
            console.info(`Found first screen paint on ${event.url}.`);
            console.info(`The navigation start time is ${event.navigationStartTime}.`);
            console.info(`The first screen paint time is ${event.firstScreenPaintTime}.`);
          }
        })
    }
  }
}
```

## onFullScreenEnter

```TypeScript
default onFullScreenEnter(callback: OnFullScreenEnterCallback | undefined): this
```

通知开发者Web组件进入全屏模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnFullScreenEnterCallback](arkts-arkweb-onfullscreenentercallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
          // 保存handler供后续退出全屏使用
          this.handler = event.handler;
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, FullScreenEnterEvent, FullScreenExitHandler } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  handler: FullScreenExitHandler | null = null;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFullScreenEnter((event: FullScreenEnterEvent): void => {
          console.info("onFullScreenEnter videoWidth: " + event.videoWidth +
            ", videoHeight: " + event.videoHeight);
          // 应用可以通过 this.handler.exitFullScreen() 主动退出全屏。
          this.handler = event.handler;
        })
    }
  }
}
```

## onFullScreenExit

```TypeScript
default onFullScreenExit(callback: (() => void) | undefined): this
```

通知开发者Web组件退出全屏模式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
            this.handler.exitFullScreen(); // 退出全屏模式
          }
        })
        .onFullScreenEnter((event) => {
          this.handler = event.handler;
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, FullScreenEnterEvent, FullScreenExitHandler } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  private handler: FullScreenExitHandler = new FullScreenExitHandler();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onFullScreenExit((): void => {
          console.info("onFullScreenExit...")
          if (this.handler) {
            this.handler.exitFullScreen();
          }
        })
        .onFullScreenEnter((event: FullScreenEnterEvent): void => {
          this.handler = event.handler;
        })
    }
  }
}
```

## onGeolocationHide

```TypeScript
default onGeolocationHide(callback: (() => void) | undefined): this
```

Called to notify the user that the request for obtaining the geolocation information received when [onGeolocationShow](#ongeolocationshow) is called has been canceled.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default onGeolocationShow(callback: Callback<OnGeolocationShowEvent> | undefined): this
```

Called when a request to obtain the geolocation information is received.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnGeolocationShowEvent](arkts-arkweb-web-ongeolocationshowevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

  // 组件的生命周期函数，创建组件实例后触发
  aboutToAppear(): void {
    let context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    if (!context) {
      console.error("context is undefined");
      return;
    }
    // 请求位置权限，对整个应用生效
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
      // Web组件的geolocationAccess属性默认为true，可以显式配置为false以禁止Web组件获取地理位置信息
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .geolocationAccess(true)
        .onGeolocationShow((event) => {
          // 位置权限申请通知仅对当前Web组件生效，应用内的其他Web组件不受影响
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              confirm: {
                value: 'onConfirm',
                action: () => {
                  // 允许此站点位置权限请求
                  // invoke的第三个参数表示是否记住当前弹窗的选择状态，传入true则下次不再弹出对话框
                  event.geolocation.invoke(event.origin, true, false);
                }
              },
              cancel: () => {
                // 不允许此站点位置权限请求
                // invoke的第三个参数表示是否记住当前弹窗的选择状态，传入true则下次不再弹出对话框
                event.geolocation.invoke(event.origin, false, false);
              }
            })
          }
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, UIContext, AlertDialogParamWithButtons, OnGeolocationShowEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      // Web组件的geolocationAccess属性默认为true，可以显式配置为false以禁止Web组件获取地理位置信息
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .geolocationAccess(true)
        .onGeolocationShow((event) => {
          // 位置权限申请通知仅对当前Web组件生效，应用内的其他Web组件不受影响
          if (event) {
            this.uiContext.showAlertDialog({
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'cancel',
                action: () => {
                  // 不允许此站点位置权限请求
                  // invoke的第三个参数表示是否记住当前弹窗的选择状态，传入true则下次不再弹出对话框
                  event.geolocation.invoke(event.origin, false, true);
                }
              },
              secondaryButton: {
                value: 'ok',
                action: () => {
                  // 允许此站点位置权限请求
                  // invoke的第三个参数表示是否记住当前弹窗的选择状态，传入true则下次不再弹出对话框
                  event.geolocation.invoke(event.origin, true, true);
                }
              },
              cancel: () => {
                // 不允许此站点位置权限请求
                // invoke的第三个参数表示是否记住当前弹窗的选择状态，传入true则下次不再弹出对话框
                event.geolocation.invoke(event.origin, false, true);
              }
            } as AlertDialogParamWithButtons)
          }
        })
    }
  }
}
```

加载的html文件。

```TypeScript
<!DOCTYPE html>
<html>
<body>
<p id="locationInfo">位置信息</p>
<button onclick="getLocation()">获取位置</button>
<script>
var locationInfo=document.getElementById("locationInfo");
function getLocation(){
  if (navigator.geolocation) {
    // 前端页面访问设备地理位置
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
default onHttpAuthRequest(callback: Callback<OnHttpAuthRequestEvent, boolean> | undefined): this
```

Triggered when the browser needs credentials from the user.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnHttpAuthRequestEvent](arkts-arkweb-web-onhttpauthrequestevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Button, Web, Column, Component, Entry, State, AppStorage, UIContext, AlertDialogParamWithButtons, OnHttpAuthRequestEvent } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();
  httpAuth: boolean = false;

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onHttpAuthRequest((event: OnHttpAuthRequestEvent):boolean => {
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
            } as AlertDialogParamWithButtons);
          }
          return true;
        })
    }
  }
}
```

## onHttpErrorReceive

```TypeScript
default onHttpErrorReceive(callback: Callback<OnHttpErrorReceiveEvent> | undefined): this
```

Triggered when the web page receives a web resource loading HTTP error.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnHttpErrorReceiveEvent](arkts-arkweb-web-onhttperrorreceiveevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, OnHttpErrorReceiveEvent } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onHttpErrorReceive((event: OnHttpErrorReceiveEvent): void  => {
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
default onInputmethodAttached(callback: OnInputmethodAttachedCallback | undefined): this
```

The callback is triggered when the inputmethod is attached to the IMF.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnInputmethodAttachedCallback](arkts-arkweb-oninputmethodattachedcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

## onIntelligentTrackingPreventionResult

```TypeScript
default onIntelligentTrackingPreventionResult(callback: OnIntelligentTrackingPreventionCallback | undefined): this
```

Called when tracker's cookie is prevented.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnIntelligentTrackingPreventionCallback](arkts-arkweb-onintelligenttrackingpreventioncallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
      // 需要打开智能防跟踪功能，才会触发onIntelligentTrackingPreventionResult回调。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';
import { Button, Web, Column, Component, Entry } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      // 需要打开智能防跟踪功能，才会触发onIntelligentTrackingPreventionResult回调。
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
default onInterceptKeyboardAttach(callback: WebKeyboardCallback | undefined): this
```

Editable elements (such as input labels) in web pages will call back to this interface before pulling up the soft keyboard. Applications can use this interface to intercept the pop-up of the system soft keyboard and configure the application-customized soft keyboard (according to this interface, the application can decide to use the system default soft keyboard/the system soft keyboard with the enter key customized/all the soft keyboards customized by the application).

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [WebKeyboardCallback](arkts-arkweb-webkeyboardcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
     * 自定义键盘组件Builder。
     */
    @Builder
    customKeyboardBuilder() {
        // 这里实现自定义键盘组件，对接WebKeyboardController实现输入、删除、关闭等操作。
      Row() {
        Text("完成")
          .fontSize(20)
          .fontColor(Color.Blue)
          .onClick(() => {
            this.webKeyboardController.close();
          })
        // 插入字符。
        Button("insertText").onClick(() => {
          this.webKeyboardController.insertText('insert ');
        }).margin({
          bottom: 200,
        })
        // 从后往前删除length参数指定长度的字符。
        Button("deleteForward").onClick(() => {
          this.webKeyboardController.deleteForward(1);
        }).margin({
          bottom: 200,
        })
        // 从前往后删除length参数指定长度的字符。
        Button("deleteBackward").onClick(() => {
          this.webKeyboardController.deleteBackward(1);
        }).margin({
          left: -220,
        })
        // 插入功能按键。
        Button("sendFunctionKey").onClick(() => {
          this.webKeyboardController.sendFunctionKey(6);
        })
      }
    }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
      .onInterceptKeyboardAttach((KeyboardCallbackInfo) => {
        // option初始化，默认使用系统默认键盘。
        let option: WebKeyboardOptions = {
          useSystemKeyboard: true,
        };
        if (!KeyboardCallbackInfo) {
          return option;
        }

        // 保存WebKeyboardController，使用自定义键盘时候，需要使用该handler控制输入、删除、软键盘关闭等行为。
        this.webKeyboardController = KeyboardCallbackInfo.controller
        let attributes: Record<string, string> = KeyboardCallbackInfo.attributes
        // 遍历attributes。
        let attributeKeys = Object.keys(attributes)
        for (let i = 0; i < attributeKeys.length; i++) {
          console.info('WebCustomKeyboard key = ' + attributeKeys[i] + ', value = ' + attributes[attributeKeys[i]])
        }

        if (attributes) {
          if (attributes['data-keyboard'] == 'customKeyboard') {
            // 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有data-keyboard，且值为customKeyboard，则使用自定义键盘。
            console.info('WebCustomKeyboard use custom keyboard')
            option.useSystemKeyboard = false;
            // 设置自定义键盘builder。
            option.customKeyboard = () => {
              this.customKeyboardBuilder()
            }
            return option;
          }

          if (attributes['keyboard-return'] != undefined) {
            // 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有keyboard-return，使用系统键盘，并且指定系统软键盘enterKey类型。
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { WebKeyboardOptions, WebKeyboardCallbackInfo, WebKeyboardController, $rawfile, Web, Column, Margin, Button, Color, Text, Row, Builder, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { inputMethodEngine } from '@kit.IMEKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  webKeyboardController: WebKeyboardController = new WebKeyboardController();
  inputAttributeMap: Map<string, int> = new Map<string, int>([
      ['UNSPECIFIED', inputMethodEngine.ENTER_KEY_TYPE_UNSPECIFIED],
      ['GO', inputMethodEngine.ENTER_KEY_TYPE_GO],
      ['SEARCH', inputMethodEngine.ENTER_KEY_TYPE_SEARCH],
      ['SEND', inputMethodEngine.ENTER_KEY_TYPE_SEND],
      ['NEXT', inputMethodEngine.ENTER_KEY_TYPE_NEXT],
      ['DONE', inputMethodEngine.ENTER_KEY_TYPE_DONE],
      ['PREVIOUS', inputMethodEngine.ENTER_KEY_TYPE_PREVIOUS]
    ])

  /**
   * 自定义键盘组件Builder。
   */
  @Builder
  customKeyboardBuilder() {
    // 这里实现自定义键盘组件，对接WebKeyboardController实现输入、删除、关闭等操作。
    Row() {
      Text("完成")
        .fontSize(20)
        .fontColor(Color.Blue)
        .onClick(() => {
          this.webKeyboardController.close();
        })
      // 插入字符。
      Button("insertText").onClick(() => {
        this.webKeyboardController.insertText('insert ');
      }).margin({
        bottom: 200,
      } as Margin)
      // 从后往前删除length参数指定长度的字符。
      Button("deleteForward").onClick(() => {
        this.webKeyboardController.deleteForward(1);
      }).margin({
        bottom: 200,
      } as Margin)
      // 从前往后删除length参数指定长度的字符。
      Button("deleteBackward").onClick(() => {
        this.webKeyboardController.deleteBackward(1);
      }).margin({
        left: -220,
      } as Margin)
      // 插入功能按键。
      Button("sendFunctionKey").onClick(() => {
        this.webKeyboardController.sendFunctionKey(6);
      })
    }
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
      .onInterceptKeyboardAttach((KeyboardCallbackInfo) => {
        // option初始化，默认使用系统默认键盘。
        let option: WebKeyboardOptions = {
          useSystemKeyboard: true,
        };
        if (!KeyboardCallbackInfo) {
          return option;
        }

        // 保存WebKeyboardController，使用自定义键盘时候，需要使用该handler控制输入、删除、软键盘关闭等行为。
        this.webKeyboardController = KeyboardCallbackInfo.controller
        let attributes: Record<string, string> = KeyboardCallbackInfo.attributes
        // 遍历attributes。
        let attributeKeys = Object.keys(attributes)
        for (let i = 0; i < attributeKeys.length; i++) {
          console.info('WebCustomKeyboard key = ' + attributeKeys[i] + ', value = ' + attributes[attributeKeys[i]])
        }

        if (attributes) {
          if (attributes['data-keyboard'] == 'customKeyboard') {
            // 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有data-keyboard，且值为customKeyboard，则使用自定义键盘。
            console.info('WebCustomKeyboard use custom keyboard')
            option.useSystemKeyboard = false;
            // 设置自定义键盘builder。
            option.customKeyboard = () => {
              this.customKeyboardBuilder()
            }
            return option;
          }

          if (attributes['keyboard-return'] != undefined) {
            // 根据html可编辑元素的属性，判断使用不同的软键盘，例如这里如果属性包含有keyboard-return，使用系统键盘，并且指定系统软键盘enterKey类型。
            option.useSystemKeyboard = true;
            let enterKeyType: int | undefined = this.inputAttributeMap.get(attributes['keyboard-return'] as string)
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

加载的html文件。

```TypeScript
<!-- index.html -->
  <!DOCTYPE html>
  <html>

  <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0">
  </head>

  <body>

  <p style="font-size:12px">input标签，原有默认行为：</p>
  <input type="text" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key UNSPECIFIED：</p>
  <input type="text" keyboard-return="UNSPECIFIED" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key GO：</p>
  <input type="text" keyboard-return="GO" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key SEARCH：</p>
  <input type="text" keyboard-return="SEARCH" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key SEND：</p>
  <input type="text" keyboard-return="SEND" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key NEXT：</p>
  <input type="text" keyboard-return="NEXT" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key DONE：</p>
  <input type="text" keyboard-return="DONE" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input标签，系统键盘自定义enterKeyType属性 enter key PREVIOUS：</p>
  <input type="text" keyboard-return="PREVIOUS" style="width: 300px; height: 20px"><br>
  <hr style="height:2px;border-width:0;color:gray;background-color:gray">

  <p style="font-size:12px">input标签，应用自定义键盘：</p>
  <input type="text" data-keyboard="customKeyboard" style="width: 300px; height: 20px"><br>

  </body>

  </html>
```

## onInterceptKeyEvent

```TypeScript
default onInterceptKeyEvent(callback: ((event: KeyEvent) => boolean) | undefined): this
```

Key events notify the application before the WebView consumes them.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((event: KeyEvent) = & gt; boolean) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, KeyEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onInterceptKeyEvent((event: KeyEvent): boolean => {
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
default onInterceptRequest(callback: Callback<OnInterceptRequestEvent, WebResourceResponse | null> | undefined): this
```

Triggered when the resources loading is intercepted.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnInterceptRequestEvent](arkts-arkweb-web-oninterceptrequestevent-i.md), [WebResourceResponse](arkts-arkweb-web-webresourceresponse-c.md) \| null & gt; \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  responseWeb: webview.WebResourceResponse = new webview.WebResourceResponse();
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
          // 将新元素追加到数组的末尾，并返回数组的新长度。
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Button, Web, Column, Component, Entry, WebResourceResponse, Header, Promise, Function } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  responseWeb: WebResourceResponse = new WebResourceResponse();
  heads: Header[] = [
    {
      headerKey: "Connection",
      headerValue: "keep-alive"
    },
    {
      headerKey: "Cache-Control",
      headerValue: "no-cache"
    }
  ] as Header[]
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
          // 将新元素追加到数组的末尾，并返回数组的新长度。
          let length = this.heads.push(head1);
          length = this.heads.push(head2);
          console.info('The response header result length is :' + length);
          const promise = new Promise<string>((resolve: Function, reject: Function) => {
            this.responseWeb.setResponseHeader(this.heads);
            this.responseWeb.setResponseData(this.webData);
            this.responseWeb.setResponseEncoding('utf-8');
            this.responseWeb.setResponseMimeType('text/html');
            this.responseWeb.setResponseCode(200);
            this.responseWeb.setReasonMessage('OK');
            console.info('The 111response header result length is :' + length);
          }) as Promise<String>
          promise.then(() => {
            console.info("prepare response ready");
            this.responseWeb.setResponseIsReady(true);
          })
          this.responseWeb.setResponseIsReady(false);
          return null;
        })
    }
  }
}
```

## onLargestContentfulPaint

```TypeScript
default onLargestContentfulPaint(callback: OnLargestContentfulPaintCallback | undefined): this
```

Triggered when the largest content paint occurs on the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnLargestContentfulPaintCallback](arkts-arkweb-onlargestcontentfulpaintcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column,LargestContentfulPaint} from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

build() {
  Column() {
    Web({ src: 'www.example.com', controller: this.controller })
      .onLargestContentfulPaint((event:LargestContentfulPaint):void => {
        if(event) {
          console.info("onLargestContentfulPaint: [navigationStartTime]= " + event.navigationStartTime +
            ", [largestImagePaintTime]=" + event.largestImagePaintTime +
            ", [largestTextPaintTime]=" + event.largestTextPaintTime +
            ", [largestImageLoadStartTime]=" + event.largestImageLoadStartTime +
            ", [largestImageLoadEndTime]=" + event.largestImageLoadEndTime +
            ", [imageBPP]=" + event.imageBPP);
        }
      })
    }
  }
}
```

## onlineImageAccess

```TypeScript
default onlineImageAccess(onlineImageAccess: boolean | undefined): this
```

设置是否允许从网络加载图片资源（通过HTTP和HTTPS访问的资源）。当属性没有显式调用时，默认允许从网络加载图片资源。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [onlineImageAccess](#onlineimageaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: ('www.example.com'), controller: this.controller })
        .onlineImageAccess(true)
    }
  }
}
```

## onLoadFinished

```TypeScript
default onLoadFinished(callback: Callback<OnLoadFinishedEvent> | undefined): this
```

Notify the host application that a page has finished loading. This method is called only for main frame.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br>
1. Fragment navigation also triggers onLoadFinished, but onPageEnd will not be triggered.
2. onLoadFinished is triggered only once if the mainframe is automatically redirected before the page is
completely loaded. onPageEnd is triggered every navigation on mainframe.
3. When the document of a pop-up window has been modified by JavaScript before it is loaded , it will simulate the
triggering of onLoadStarted with the URL set to empty because displaying the URL that is currently loading may be unsafe. onPageBegin will not be simulated. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadFinishedEvent](arkts-arkweb-web-onloadfinishedevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, OnLoadFinishedEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onLoadFinished((event: OnLoadFinishedEvent): void => {
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
default onLoadIntercept(callback: Callback<OnLoadInterceptEvent, boolean> | undefined): this
```

Triggered when the resources loading is intercepted.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadInterceptEvent](arkts-arkweb-web-onloadinterceptevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, OnLoadInterceptEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onLoadIntercept((event: OnLoadInterceptEvent): boolean => {
          if (event) {
            console.info('url:' + event.data.getRequestUrl());
            console.info('isMainFrame:' + event.data.isMainFrame());
            console.info('isRedirect:' + event.data.isRedirect());
            console.info('isRequestGesture:' + event.data.isRequestGesture());
          }
          return true;
        })
    }
  }
}
```

## onLoadStarted

```TypeScript
default onLoadStarted(callback: Callback<OnLoadStartedEvent> | undefined): this
```

Triggered at the begin of web page loading. This method is called once for each main frame load. Embedded frame changes, i.e. clicking a link whose target is an iframe and fragment navigations (navigations to #fragment_id) will not trigger this callback.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> When the document of a pop-up window has been modified by JavaScript before it is loaded, it will simulate the triggering of onLoadStarted with the URL set to empty because displaying the URL that is currently loading maybe unsafe. onPageBegin will not be simulated. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnLoadStartedEvent](arkts-arkweb-web-onloadstartedevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, OnLoadStartedEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onLoadStarted((event: OnLoadStartedEvent): void => {
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
default onMicrophoneCaptureStateChange(callback: OnMicrophoneCaptureStateChangeCallback | undefined): this
```

通知用户当前网页中麦克风状态，麦克风有三个状态，未工作（None），捕获中（Active），暂停中（Paused）。使用callback异步回调。可以通过resumeMicrophone，pauseMicrophone，stopMicrophone这三个接口来切换麦克风的状态。这三个接口功能分别对应解除暂停，暂停，停止麦克风。示例使用场景详见 [网页中麦克风的使用](../../../reference/apis-arkweb/arkts-apis-webview-WebviewController.md#resumemicrophone)。

> **说明：**&gt;
> 当前网页正在使用麦克风时，返回捕获中状态；当前网页暂停使用麦克风时，返回暂停中状态；当前网页完全没有使用麦克风时，返回未工作状态。&gt;
> 当前麦克风处于捕获中状态时，设置暂停使用，当前麦克风变为暂停中状态。可通过ArkWeb设置麦克风开始使用状态进行恢复捕捉。&gt;
> 当前麦克风处于捕获中状态时，设置停止使用，当前麦克风停止捕捉，麦克风变为未工作状态。除非重新前端开始捕捉，否则无法恢复。&gt;
> 当前麦克风处于暂停中状态时，设置开始使用，当前麦克风继续捕捉，变为捕获中状态。&gt;
> 当前麦克风处于暂停中状态时，设置停止使用，当前麦克风停止捕捉，变为未工作状态。除非重新前端开始捕捉，否则无法恢复。&gt;
> 当前麦克风处于未工作状态时，设置开始使用以及暂停使用，麦克风状态均不发生变化。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnMicrophoneCaptureStateChangeCallback](arkts-arkweb-onmicrophonecapturestatechangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
        .onMicrophoneCaptureStateChange((event: MicrophoneCaptureStateInfo) => {
          console.info("Microphone from ", event.originalState, " to ", event.newState);
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, Button, OnPermissionRequestEvent, Context } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { UIContext } from "@kit.ArkUI";
import { AlertDialogParamWithButtons, AlertDialogButtonBaseOptions } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { PermissionRequestResult, common, abilityAccessCtrl } from '@kit.AbilityKit';
import { MicrophoneCaptureStateChangeInfo } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(context, ['ohos.permission.MICROPHONE'],
      (err: BusinessError | null, data?: PermissionRequestResult) => {
        if (data) {
          console.info('data:' + JSON.stringify(data));
          console.info('data permissions:' + data.permissions);
          console.info('data authResults:' + data.authResults);
        }
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
        .onPermissionRequest((event: OnPermissionRequestEvent): void => {
          if (event) {
            const dialogOptions: AlertDialogParamWithButtons = {
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                },
              } as AlertDialogButtonBaseOptions,
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                },
              } as AlertDialogButtonBaseOptions,
              cancel: () => {
                event.request.deny();
              }
            };
            this.uiContext.showAlertDialog(dialogOptions);
          }
        })
        .onMicrophoneCaptureStateChange((event: MicrophoneCaptureStateChangeInfo | undefined): void => {
          if (event) {
            console.info("Microphone from ", event.originalState, " to ", event.newState);
          }
        })
    }
  }
}
```

加载的html文件

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
   <input type="button" title="HTML5麦克风" value="开启麦克风" onclick="getMedia()" />
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
default onNativeEmbedGestureEvent(callback: ((event: NativeEmbedTouchInfo) => void) | undefined): this
```

Triggered when gesture effect on embed tag.<p>&lt;strong&gt;API Note&lt;/strong&gt;: &lt;strong&gt;Performance Note&lt;/strong&gt;: <p>For details about how to rendering native components on the Web using same-layer rendering. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((event: NativeEmbedTouchInfo) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { NodeController, FrameNode, UIContext, TouchEvent, Component, Prop, State, Color, Column, Builder } from "@kit.ArkUI";
import {  Entry, Button, Stack, NodeContainer, Web, $rawfile, NativeEmbedStatus, TouchType, wrapBuilder, NativeEmbedTouchInfo } from "@kit.ArkUI";
import { NodeRenderType, RenderOptions, BuilderNode } from 'arkui.BuilderNode';

export class Params {
  text: string = '';
  width: double = 1;
  height: double = 1;
}

export class NodeControllerParams {
  surfaceId: string = '';
  renderType: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  width: double = 0;
  height: double = 0;
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<Params> | undefined | null = null;
  private surfaceId_: string = "";
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: double = 0;
  private height_: double = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode<Params>(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ } );
    this.rootNode?.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ } as Params);
    return this.rootNode?.getFrameNode() ?? null;
  }

  postInputEvent(event: TouchEvent): boolean {
    return this.rootNode?.postInputEvent(event) ?? false;
  }
}

@Component
struct ButtonComponent {
  @Prop params: Params = {} as Params;
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
    .backgroundColor(Color.Green)
  }
}

@Builder
function ButtonBuilder(params: Params) {
  ButtonComponent({ params: params })
}

@Entry
@Component
struct WebComponent {
  @State eventType: string = '';
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
                width: this.uiContext!.px2vp(embed.info?.width ?? 0),
                height: this.uiContext!.px2vp(embed.info?.height ?? 0)
              });
              this.nodeController.rebuild();
            }
          })
          .onNativeEmbedGestureEvent((event: NativeEmbedTouchInfo) => {
            if (event && event.touchEvent) {
              if (event.touchEvent?.type == TouchType.Down) {
                this.eventType = 'Down'
              }
              if (event.touchEvent?.type == TouchType.Up) {
                this.eventType = 'Up'
              }
              if (event.touchEvent?.type == TouchType.Move) {
                this.eventType = 'Move'
              }
              if (event.touchEvent?.type == TouchType.Cancel) {
                this.eventType = 'Cancel'
              }
              let touchEvent = event.touchEvent as TouchEvent;
              let ret = this.nodeController.postInputEvent(touchEvent)
              if (event.result) {
                event.result?.setGestureEventResult(ret, true);
              }
              console.info("embedId = " + event.embedId);
              console.info("touchType = " + this.eventType);
              console.info("x = " + event.touchEvent?.touches[0].x);
              console.info("y = " + event.touchEvent?.touches[0].y);
              console.info("Component globalPos:(" + event.touchEvent?.target.area.globalPosition.x + "," +
              event.touchEvent?.target.area.globalPosition.y + ")");
              console.info("width = " + event.touchEvent?.target.area.width);
              console.info("height = " + event.touchEvent?.target.area.height);
            }
          })
      }
    }
  }
}
```

加载的html文件

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>同层渲染测试html</title>
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
default onNativeEmbedLifecycleChange(callback: ((event: NativeEmbedDataInfo) => void) | undefined): this
```

Triggered when embed lifecycle changes.<p>&lt;strong&gt;API Note&lt;/strong&gt;: &lt;strong&gt;Performance Note&lt;/strong&gt;: <p>For details about how to rendering native components on the Web using same-layer rendering. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | ((event: NativeEmbedDataInfo) = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// EntryAbility.ets

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    // API12新增：开启同层渲染BFCache开关
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

ArkTS-Sta示例：

```TypeScript
// EntryAbility.ets
'use static'
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
    // API12新增：开启同层渲染BFCache开关
    let features = new webview.BackForwardCacheSupportedFeatures();
    features.nativeEmbed = true;
    features.mediaTakeOver = true;
    webview.WebviewController.enableBackForwardCache(features);
    webview.WebviewController.initializeWebEngine();
  }

  onDestroy(): Promise<void>|undefined {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
    return undefined;
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    windowStage.loadContent('pages/Index', (err) => {
      if (err?.code) {
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

ArkTS-Dyn示例：

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
      // 默认行为：点击按钮跳转页面，关闭index页面，使同层标签销毁。
      // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮跳转页面，关闭index页面，使同层标签进入BFCache。
      Button('Destroy')
      .onClick(() => {
        try {
          this.controller.loadUrl("www.example.com");
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })

      // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮返回页面，使同层标签离开BFCache。
      Button('backward')
      .onClick(() => {
        try {
          this.controller.backward();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })

      // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮前进页面，使同层标签进入BFCache。
      Button('forward')
      .onClick(() => {
        try {
          this.controller.forward();
        } catch (error) {
          console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
        }
      })


      // API12新增同层标签进入离开BFCache状态：非http与https协议加载的网页，Web内核不支持进入BFCache;
      // 因此如果要测试ENTER_BFCACHE/LEAVE_BFCACHE状态，需要将index.html放到Web服务器上，使用http或者https协议加载，如：
      // Web({ src: "http://xxxx/index.html", controller: this.controller })
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableNativeEmbedMode(true)
        .onNativeEmbedLifecycleChange((event) => {
          // 当加载页面中有同层标签会触发Create。
          if (event.status == NativeEmbedStatus.CREATE) {
            this.embedStatus = 'Create';
          }
          // 当页面中同层标签移动或者缩放时会触发Update。
          if (event.status == NativeEmbedStatus.UPDATE) {
            this.embedStatus = 'Update';
          }
          // 退出页面时会触发Destroy。
          if (event.status == NativeEmbedStatus.DESTROY) {
            this.embedStatus = 'Destroy';
          }
          // 同层标签所在的页面进入BFCache时，会触发Enter BFCache。
          if (event.status == NativeEmbedStatus.ENTER_BFCACHE) {
            this.embedStatus = 'Enter BFCache';
          }
          // 同层标签所在的页面离开BFCache时，会触发Leave BFCache。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile,State, Entry, Column, Component, Button, Web, NativeEmbedStatus, NativeEmbedDataInfo } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  @State embedStatus: string = '';
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      // 默认行为：点击按钮跳转页面，关闭index页面，使同层标签销毁。
      // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮跳转页面，关闭index页面，使同层标签进入BFCache。
      Button('Destroy')
        .onClick(() => {
          try {
            this.controller.loadUrl("www.example.com");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })

      // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮返回页面，使同层标签离开BFCache。
      Button('backward')
        .onClick(() => {
          try {
            this.controller.backward();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })

      // API12新增：使能同层渲染所在的页面支持BFCache后，点击按钮前进页面，使同层标签进入BFCache。
      Button('forward')
        .onClick(() => {
          try {
            this.controller.forward();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })


      // API12新增同层标签进入离开BFCache状态：非http与https协议加载的网页，Web内核不支持进入BFCache;
      // 因此如果要测试ENTER_BFCACHE/LEAVE_BFCACHE状态，需要将index.html放到Web服务器上，使用http或者https协议加载，如：
      // Web({ src: "http://xxxx/index.html", controller: this.controller })
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .enableNativeEmbedMode(true)
        .onNativeEmbedLifecycleChange((event:NativeEmbedDataInfo):void => {
          // 当加载页面中有同层标签会触发Create。
          if (event.status == NativeEmbedStatus.CREATE) {
            this.embedStatus = 'Create';
          }
          // 当页面中同层标签移动或者缩放时会触发Update。
          if (event.status == NativeEmbedStatus.UPDATE) {
            this.embedStatus = 'Update';
          }
          // 退出页面时会触发Destroy。
          if (event.status == NativeEmbedStatus.DESTROY) {
            this.embedStatus = 'Destroy';
          }
          // 同层标签所在的页面进入BFCache时，会触发Enter BFCache。
          if (event.status == NativeEmbedStatus.ENTER_BFCACHE) {
            this.embedStatus = 'Enter BFCache';
          }
          // 同层标签所在的页面离开BFCache时，会触发Leave BFCache。
          if (event.status == NativeEmbedStatus.LEAVE_BFCACHE) {
            this.embedStatus = 'Leave BFCache';
          }
          console.info("status = " + this.embedStatus);
          console.info("surfaceId = " + event.surfaceId);
          console.info("embedId = " + event.embedId);
          if (event.info) {
            console.info("id = " + event.info?.id);
            console.info("type = " + event.info?.type);
            console.info("src = " + event.info?.src);
            console.info("width = " + event.info?.width);
            console.info("height = " + event.info?.height);
            console.info("url = " + event.info?.url);
          }
        })
    }
  }
}
```

加载的html文件

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>同层渲染测试html</title>
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
default onNativeEmbedMouseEvent(callback: MouseInfoCallback | undefined): this
```

Triggered when mouse effect on embed tag.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [MouseInfoCallback](arkts-arkweb-mouseinfocallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Web, Column, Component, Entry } from '@ohos.arkui.component';
import webview from '@ohos.web.webview';
import { State } from '@ohos.arkui.stateManagement';
import { NodeController, FrameNode, UIContext, TouchEvent, MouseEvent, Prop, Color, Button, Stack, NodeContainer, NativeEmbedStatus, wrapBuilder } from '@kit.ArkUI';
import { BuilderNode, NodeRenderType } from '@ohos.arkui.node';

export class Params {
  text: string = '';
  width: double = 1;
  height: double = 1;
}

export class NodeControllerParams {
  surfaceId: string = '';
  renderType: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  width: double = 0;
  height: double = 0;
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<Params> | null = null;
  private surfaceId_: string = "";
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: double = 0;
  private height_: double = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode<Params>(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
    this.rootNode?.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
    return this.rootNode?.getFrameNode() ?? null;
  }

  postInputEvent(event: MouseEvent): boolean {
    return this.rootNode?.postInputEvent(event) ?? false;
  }
}

@Component
struct ButtonComponent {
  @Prop params: Params = {} as Params;
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
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  private nodeController: MyNodeController = new MyNodeController();
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Stack() {
        NodeContainer(this.nodeController)
        Web({ src: 'resource://rawfile/index.html', controller: this.controller })
          .enableNativeEmbedMode(true)
          .onNativeEmbedLifecycleChange((embed) => {
            if (embed.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: embed.surfaceId as string,
                renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                width: this.uiContext!.px2vp(embed.info?.width ?? 0),
                height: this.uiContext!.px2vp(embed.info?.height ?? 0),
              });
              this.nodeController.rebuild();
            }
          })
          .onNativeEmbedMouseEvent((event) => {
            if (event && event.mouseEvent) {
              const mouseEvent = event.mouseEvent as MouseEvent;
              let ret = this.nodeController.postInputEvent(mouseEvent)
              if (event.result) {
                event.result?.setMouseEventResult(ret, true);
              }
            }
          })
      }
    }
  }
}
```

加载的html文件

```TypeScript
<!-- index.html -->
<!Document>
<html>
<head>
    <title>同层渲染测试</title>
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
default onNativeEmbedObjectParamChange(callback: OnNativeEmbedObjectParamChangeCallback | undefined): this
```

Triggered when the param element which is a child item of the object element has changed.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnNativeEmbedObjectParamChangeCallback](arkts-arkweb-onnativeembedobjectparamchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
import { Entry, Column, Component, Web } from '@ohos.arkui.component'
  import webview from '@ohos.web.webview';
  import { State } from '@ohos.arkui.stateManagement';
  import { NodeController, FrameNode, UIContext, TouchEvent, MouseEvent, Prop, Color, Button, Stack, NodeContainer, NativeEmbedStatus, wrapBuilder } from '@kit.ArkUI';
  import { BuilderNode, NodeRenderType } from '@ohos.arkui.node';


  export class Params {

    text: string = '';
    width: double = 1;
    height: double = 1;
  }

  export class NodeControllerParams {
    surfaceId: string = '';
    renderType: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
    width: double = 0;
    height: double = 0;
  }

  class MyNodeController extends NodeController {
    private rootNode: BuilderNode<Params>  | null = null;
    private surfaceId_: string = "";
    private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
    private width_: double = 0;
    private height_: double = 0;

    setRenderOption(params: NodeControllerParams) {
      this.surfaceId_ = params.surfaceId;
      this.renderType_ = params.renderType;
      this.width_ = params.width;
      this.height_ = params.height;
    }

    makeNode(uiContext: UIContext): FrameNode | null {
      this.rootNode = new BuilderNode<Params>(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ } );
      this.rootNode?.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ } as Params);
      return this.rootNode?.getFrameNode() ?? null;
    }

    postInputEvent(event: TouchEvent): boolean {
      return this.rootNode?.postInputEvent(event) ?? false;
    }
  }

  @Component
  struct ButtonComponent {
    @Prop params: Params = {} as Params;
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
    controller: webview.WebviewController = new webview.WebviewController(undefined);
    private nodeController: MyNodeController = new MyNodeController();
    uiContext: UIContext = this.getUIContext();

    build() {
      Column() {

        Stack() {
          NodeContainer(this.nodeController)
          Web({ src: 'resource://rawfile/index.html', controller: this.controller })
            .enableNativeEmbedMode(true)
            .registerNativeEmbedRule("object", "native")
            .onNativeEmbedLifecycleChange((embed) => {
              if (embed.status == NativeEmbedStatus.CREATE) {
                this.nodeController.setRenderOption({
                  surfaceId: embed.surfaceId as string,
                  renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                  width: this.uiContext!.px2vp(embed.info?.width ?? 0),
                  height: this.uiContext!.px2vp(embed.info?.height ?? 0)
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

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>同层渲染测试</title>
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
default onNativeEmbedVisibilityChange(callback: OnNativeEmbedVisibilityChangeCallback | undefined): this
```

Called when the visibility of a same-layer tag (such as an Embed tag or an Object tag) on a web page changes in the viewport. By default, the same-layer tag is invisible. If the rendering tag is visible when you access the page for the first time, the callback is triggered; otherwise, it is not triggered. That is, if the same-layer tag changes from a non-zero value to 0 x 0, the callback is triggered. If the rendering tag size changes from 0 x 0 to a non-zero value, the callback is not triggered. If all the same-layer tags are invisible, they are reported as invisible. If all the same-layer rendering tags or part of them are visible, they are reported as invisible.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnNativeEmbedVisibilityChangeCallback](arkts-arkweb-onnativeembedvisibilitychangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { $rawfile, State, Entry, Column, Component, Button, Web, NativeEmbedStatus, NativeEmbedDataInfo } from '@kit.ArkUI';
import { NodeController, UIContext, FrameNode, TouchEvent, Prop, Color, Builder, wrapBuilder, Stack, NodeContainer } from '@kit.ArkUI';
import { NodeRenderType, RenderOptions, BuilderNode } from 'arkui.BuilderNode';

export class Params {
  text: string = '';
  width: double = 1;
  height: double = 1;
}

export class NodeControllerParams {
  surfaceId: string = '';
  renderType: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  width: double = 0;
  height: double = 0;
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<Params> | undefined | null = null;
  private surfaceId_: string = "";
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: double = 0;
  private height_: double = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode<Params>(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ } );
    this.rootNode?.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ } as Params);
    return this.rootNode?.getFrameNode() ?? null;
  }

  postInputEvent(event: TouchEvent): boolean {
    return this.rootNode?.postInputEvent(event) ?? false;
  }
}

@Component
struct ButtonComponent {
  @Prop params: Params = {} as Params;
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
    .backgroundColor(Color.Green)
  }
}

@Builder
function ButtonBuilder(params: Params) {
  ButtonComponent({ params: params })
}

@Entry
@Component
struct WebComponent {
  @State embedVisibility: string = '';
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
                width: this.uiContext!.px2vp(embed.info?.width ?? 0),
                height: this.uiContext!.px2vp(embed.info?.height ?? 0)
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

加载的html文件

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>同层渲染测试html</title>
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
default onNavigationEntryCommitted(callback: OnNavigationEntryCommittedCallback | undefined): this
```

Called when the load committed.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnNavigationEntryCommittedCallback](arkts-arkweb-onnavigationentrycommittedcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default onOverrideErrorPage(callback: OnOverrideErrorPageCallback | undefined): this
```

Triggered when the web page's document resource error. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> This only triggered for main frame. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnOverrideErrorPageCallback](arkts-arkweb-onoverrideerrorpagecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  build() {
    Column() {
      Web({ src: $rawfile("iframe_error.html"), controller: this.controller })
        .onControllerAttached(() => {
          // 启用mainframe错误页功能，并同时启用subframe错误页功能
          this.controller.setErrorPageEnabled(true, true);
        })
        .onOverrideErrorPage((event) => {
          let errorCode: number = event.error.getErrorCode();
          if (event.request.isMainFrame()) {
            // mainframe加载失败，返回mainframe自定义错误页
            return "<html><body><h1>主页面加载失败</h1><p>错误码：" + errorCode + "</p></body></html>";
          }
          // subframe加载失败，返回subframe自定义错误页
          return "<html><body><h1>子页面加载失败</h1><p>错误码：" + errorCode + "</p></body></html>";
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, $rawfile } from '@kit.ArkUI';
@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  build() {
    Column() {
      Web({ src: $rawfile("iframe_error.html"), controller: this.controller })
        .onControllerAttached(() => {
          // 启用mainframe错误页功能，并同时启用subframe错误页功能
          this.controller.setErrorPageEnabled(true, true);
        })
        .onOverrideErrorPage((event) => {
          let errorCode: number = event.error.getErrorCode();
          if (event.request.isMainFrame()) {
            // mainframe加载失败，返回mainframe自定义错误页
            return "<html><body><h1>主页面加载失败</h1><p>错误码：" + errorCode + "</p></body></html>";
          }
          // subframe加载失败，返回subframe自定义错误页
          return "<html><body><h1>子页面加载失败</h1><p>错误码：" + errorCode + "</p></body></html>";
        })
    }
  }
}
```

## onOverrideUrlLoading

```TypeScript
default onOverrideUrlLoading(callback: OnOverrideUrlLoadingCallback | undefined): this
```

When the URL is about to be loaded into the current Web, it gives the application the opportunity to take control. This will not called for POST requests, may be called for subframes and with non-HTTP(S) schemes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnOverrideUrlLoadingCallback](arkts-arkweb-onoverrideurlloadingcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, WebResourceRequest, $rawfile } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .onOverrideUrlLoading((webResourceRequest: WebResourceRequest): boolean => {
          if (webResourceRequest && webResourceRequest.getRequestUrl() == "about:blank") {
            return true;
          }
          return false;
        })
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>测试网页</title>
</head>
<body>
  <h1>onOverrideUrlLoading Demo</h1>
  <a href="about:blank">Click here</a>// 访问about:blank。
</body>
</html>
```

## onOverScroll

```TypeScript
default onOverScroll(callback: Callback<OnOverScrollEvent> | undefined): this
```

Triggered when the over scrolling.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnOverScrollEvent](arkts-arkweb-web-onoverscrollevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, OnOverScrollEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onOverScroll((event: OnOverScrollEvent) => {
          console.info("x = " + event.xOffset);
          console.info("y = " + event.yOffset);
        })
    }
  }
}
```

## onPageBegin

```TypeScript
default onPageBegin(callback: Callback<OnPageBeginEvent> | undefined): this
```

Called when the web page starts to be loaded. This API is called only for the main frame, and not for the iframe or frameset content.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageBeginEvent](arkts-arkweb-web-onpagebeginevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, OnPageBeginEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageBegin((event: OnPageBeginEvent): void => {
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
default onPageEnd(callback: Callback<OnPageEndEvent> | undefined): this
```

Triggered at the end of web page loading. This callback is only invoked for the main frame and not for subframes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageEndEvent](arkts-arkweb-web-onpageendevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, OnPageEndEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onPageEnd((event: OnPageEndEvent): void => {
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
default onPageVisible(callback: Callback<OnPageVisibleEvent> | undefined): this
```

Triggered when previous page will no longer be drawn and next page begin to draw.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPageVisibleEvent](arkts-arkweb-web-onpagevisibleevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default onPdfLoadEvent(callback: Callback<OnPdfLoadEvent> | undefined): this
```

通知用户PDF页面加载状态，包括成功或失败。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPdfLoadEvent](arkts-arkweb-web-onpdfloadevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // 使用时需将'https://www.example.com/xxx.pdf'替换为真实可访问的地址
      Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
        .onPdfLoadEvent((eventInfo: OnPdfLoadEvent) => {
          console.info(`Load event callback called. url: ${eventInfo.url}, result: ${eventInfo.result}.`)
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
  'use static'

  import { webview } from '@kit.ArkWeb';
  import { Entry, Text, Column, Component, Web} from '@ohos.arkui.component'
  import { OnPdfLoadEvent } from '@ohos.arkui.component'

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController(undefined);

    build() {
      Column() {
        // 使用时需将'https://www.example.com/xxx.pdf'替换为真实可访问的地址
        Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
          .onPdfLoadEvent((event: OnPdfLoadEvent) => {
            console.info(`Load event callback called. url: ${event.url}, result: ${event.result}.`)
          })
      }
    }
  }
```

## onPdfScrollAtBottom

```TypeScript
default onPdfScrollAtBottom(callback: Callback<OnPdfScrollEvent> | undefined): this
```

通知用户PDF页面已滚动到底。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPdfScrollEvent](arkts-arkweb-web-onpdfscrollevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      // 使用时需将'https://www.example.com/xxx.pdf'替换为真实可访问的地址
      Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
        .onPdfScrollAtBottom((eventInfo: OnPdfScrollEvent) => {
          console.info(`Scroll at bottom callback called. url: ${eventInfo.url}.`)
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
  'use static'

  import { webview } from '@kit.ArkWeb';
  import { Entry, Text, Column, Component, Web} from '@ohos.arkui.component'
  import { OnPdfScrollEvent } from '@ohos.arkui.component'

  @Entry
  @Component
  struct WebComponent {
    controller: webview.WebviewController = new webview.WebviewController(undefined);

    build() {
      Column(undefined) {
        // 使用时需将'https://www.example.com/xxx.pdf'替换为真实可访问的地址
        Web({ src: 'https://www.example.com/xxx.pdf', controller: this.controller })
          .onPdfScrollAtBottom((event: OnPdfScrollEvent) => {
            console.info(`Scroll at bottom callback called. url: ${event.url}.`)
          })
      }
    }
  }
```

## onPermissionRequest

```TypeScript
default onPermissionRequest(callback: Callback<OnPermissionRequestEvent> | undefined): this
```

通知收到获取权限请求，需配置"ohos.permission.CAMERA"、"ohos.permission.MICROPHONE"权限。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPermissionRequestEvent](arkts-arkweb-web-onpermissionrequestevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
    // 配置Web开启调试模式
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
                  // 用户点击拒绝，调用deny通知Web组件拒绝权限请求
                  event.request.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  // 用户点击确认，调用grant通知Web组件授予权限
                  event.request.grant(event.request.getAccessibleResource());
                }
              },
              cancel: () => {
                // 用户取消对话框，调用deny通知Web组件拒绝权限请求
                event.request.deny();
              }
            })
          }
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { $rawfile, Web, Column, Component, Entry, Button, OnPermissionRequestEvent, Context } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { UIContext } from "@kit.ArkUI";
import { AlertDialogParamWithButtons, AlertDialogButtonBaseOptions } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { PermissionRequestResult, common } from '@kit.AbilityKit';
import abilityAccessCtrl from '@ohos.abilityAccessCtrl'

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  aboutToAppear(): void {
    let context: Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;
    let atManager: abilityAccessCtrl.AtManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(context, ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE'],
      (err: BusinessError | null, data?: PermissionRequestResult) => {
        if (data) {
          console.info('data:' + JSON.stringify(data));
          console.info('data permissions:' + data.permissions);
          console.info('data authResults:' + data.authResults);
        }
      })
  }

  build() {
    Column() {
      Web({ src: $rawfile('index.html'), controller: this.controller })
        .onPermissionRequest((event: OnPermissionRequestEvent): void => {
          if (event) {
            const dialogOptions: AlertDialogParamWithButtons = {
              title: 'title',
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.request.deny();
                },
              } as AlertDialogButtonBaseOptions,
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.request.grant(event.request.getAccessibleResource());
                },
              } as AlertDialogButtonBaseOptions,
              cancel: () => {
                event.request.deny();
              }
            };
            this.uiContext.showAlertDialog(dialogOptions);
          }
        })
    }
  }
}
```

加载的html文件。

```TypeScript
<!-- index.html -->
 <!DOCTYPE html>
 <html>
 <head>
   <meta charset="UTF-8">
 </head>
 <body>
 <video id="video" width="500px" height="500px" autoplay="autoplay"></video>
 <canvas id="canvas" width="500px" height="500px"></canvas>
 <br>
 <input type="button" title="HTML5摄像头" value="开启摄像头" onclick="getMedia()"/>
 <script>
   function getMedia()
   {
     let constraints = {
       video: {width: 500, height: 500},
       audio: true
     };
     // 获取video摄像头区域
     let video = document.getElementById("video");
     // 返回的Promise对象
     let promise = navigator.mediaDevices.getUserMedia(constraints);
     // then()异步，调用MediaStream对象作为参数
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
default onProgressChange(callback: Callback<OnProgressChangeEvent> | undefined): this
```

Triggered when the page loading progress changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnProgressChangeEvent](arkts-arkweb-web-onprogresschangeevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Entry, Column, Component, Web, OnProgressChangeEvent } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onProgressChange((event: OnProgressChangeEvent): void => {
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
default onPrompt(callback: Callback<OnPromptEvent, boolean> | undefined): this
```

Triggered when prompt() is invoked by the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnPromptEvent](arkts-arkweb-web-onpromptevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
          value: '取消',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            console.info('Callback when the button is clicked');
            // 用户点击取消，调用handleCancel通知Web组件取消结果
            this.result?.handleCancel()
          }
        },
        {
          value: '确认',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            // 用户点击确认，调用handlePromptConfirm通知Web组件确认结果并传入用户输入的内容
            this.result?.handlePromptConfirm(this.promptResult);
          }
        }
      ],
    }),
    onWillDismiss: () => {
      // 弹窗被取消，调用handleCancel通知Web组件取消结果
      this.result?.handleCancel();
      this.dialogController.close();
    }
  });

  // 自定义弹出框的内容区
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
            this.title = "来自" + event.url + "的消息";
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, State, Column, Component, Entry, WebKeyboardAvoidMode, CustomDialogController, Builder} from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { JsResult, Text, TextInput, ButtonStyleMode } from '@kit.ArkUI';
import { CustomContentDialog } from '@ohos.arkui.advanced.Dialog';

@Entry
@Component
struct WebComponent {
  @State message: string = 'Hello World';
  @State title: string = 'Hello World';
  @State result: JsResult | null = null;
  promptResult: string = '';
  webviewController: webview.WebviewController = new webview.WebviewController(undefined);
  dialogController: CustomDialogController = new CustomDialogController({
    builder: CustomContentDialog({
      primaryTitle: this.title,
      contentBuilder: () => {
        this.buildContent();
      },
      buttons: [
        {
          value: '取消',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            console.info('Callback when the button is clicked');
            // 用户点击取消，调用handleCancel通知Web组件取消结果
            this.result?.handleCancel()
          }
        },
        {
          value: '确认',
          buttonStyle: ButtonStyleMode.TEXTUAL,
          action: () => {
            // 用户点击确认，调用handlePromptConfirm通知Web组件确认结果并传入用户输入的内容
            this.result?.handlePromptConfirm(this.promptResult);
          }
        }
      ],
    }),
    onWillDismiss: () => {
      // 弹窗被取消，调用handleCancel通知Web组件取消结果
      this.result?.handleCancel();
      this.dialogController.close();
    }
  });

  // 自定义弹出框的内容区。
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
            this.title = "来自" + event.url + "的消息";
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

加载的html文件。

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
default onRefreshAccessedHistory(callback: Callback<OnRefreshAccessedHistoryEvent> | undefined): this
```

Triggered when the Web page refreshes accessed history.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnRefreshAccessedHistoryEvent](arkts-arkweb-web-onrefreshaccessedhistoryevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
          }
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, OnRefreshAccessedHistoryEvent } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRefreshAccessedHistory((event: OnRefreshAccessedHistoryEvent): void => {
          if (event) {
            console.info('url:' + event.url + ' isReload:' + event.isRefreshed);
          }
        })
    }
  }
}
```

## onRenderExited

```TypeScript
default onRenderExited(callback: Callback<OnRenderExitedEvent> | undefined): this
```

Triggered when the render process exits. Multiple Web components may share a single rendering process, and each affected Web component will trigger the callback. When the application handles this callback, it can call the related interface of the bound webviewController to restore the page. Such as refresh, loadUrl, etc. For details of component lifecycle callback, please refer to the lifecycle of Web components.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnRenderExitedEvent](arkts-arkweb-web-onrenderexitedevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, RenderExitReason, OnRenderExitedEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined)

  build() {
    Column() {
      Web({ src: 'chrome://crash/', controller: this.controller })
        .onRenderExited((event: OnRenderExitedEvent): void => {
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
default onRenderProcessNotResponding(callback: OnRenderProcessNotRespondingCallback | undefined): this
```

Triggered when render process not responding. If the Web component can't handle the input event, or can't navigate to the new URL within a reasonable time range, the Web page process is considered unresponsive and the callback will be triggered. As long as the web process has been unresponsive, this callback may continue to trigger until the web process responds again, at which time [onRenderProcessResponding](#onrenderprocessresponding) will trigger. Applications can terminate the associated rendering process through the WebviewController interface [terminateRenderProcess](arkts-arkweb-webview-webviewcontroller-c.md#terminaterenderprocess), which may affect other Web components in the same rendering process.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnRenderProcessNotRespondingCallback](arkts-arkweb-onrenderprocessnotrespondingcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Web, RenderProcessNotRespondingData } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRenderProcessNotResponding((data: RenderProcessNotRespondingData): void => {
          console.info("onRenderProcessNotResponding: [jsStack]= " + data.jsStack +
            ", [process]=" + data.pid + ", [reason]=" + data.reason);
        })
    }
  }
}
```

## onRenderProcessResponding

```TypeScript
default onRenderProcessResponding(callback: OnRenderProcessRespondingCallback | undefined): this
```

This callback function is triggered when the rendering process changes from unresponsive state to normal operation state, which indicates that the webpage is not really stuck.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnRenderProcessRespondingCallback](arkts-arkweb-onrenderprocessrespondingcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Column, Component, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onRenderProcessResponding((): void => {
          console.info("onRenderProcessResponding again");
        })
    }
  }
}
```

## onRequestSelected

```TypeScript
default onRequestSelected(callback: (() => void) | undefined): this
```

Triggered when the Web gets the focus.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default onResourceLoad(callback: Callback<OnResourceLoadEvent> | undefined): this
```

Triggered when the url loading.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnResourceLoadEvent](arkts-arkweb-web-onresourceloadevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, OnResourceLoadEvent } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
         .onResourceLoad((event: OnResourceLoadEvent): void => {
          console.info('onResourceLoad: ' + event.url);
        })
    }
  }
}
```

## onSafeBrowsingCheckFinish

```TypeScript
default onSafeBrowsingCheckFinish(callback: OnSafeBrowsingCheckResultCallback | undefined): this
```

Triggered when the website security risk check is completed. <p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Unlike onSafeBrowsingCheckResult, which is only triggered when a URL has security risks, onSafeBrowsingCheckFinish is also triggered when the website security risk check is not performed or no risks are found.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-arkweb-onsafebrowsingcheckresultcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
        .onSafeBrowsingCheckFinish((threatType: ThreatType) => {
          console.info("onSafeBrowsingCheckFinish: [threatType]= " + threatType);
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      // 使用时需要將"https://www.example.com"替换成真实要访问的网站地址。
      Web({ src: 'www.example.com', controller: this.controller })
        .onSafeBrowsingCheckFinish((threatType: ThreatType) => {
            console.info("onSafeBrowsingCheckFinish: [threatType]= " + threatType);
        })
    }
  }
}
```

## onSafeBrowsingCheckResult

```TypeScript
default onSafeBrowsingCheckResult(callback: OnSafeBrowsingCheckResultCallback | undefined): this
```

Called when received website security risk check result.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnSafeBrowsingCheckResultCallback](arkts-arkweb-onsafebrowsingcheckresultcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
        .onSafeBrowsingCheckResult((threatType: ThreatType) => {
          console.info("onSafeBrowsingCheckResult: [threatType]= " + threatType);
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'http://example.com', controller: this.controller })
        .onSafeBrowsingCheckResult((threatType: ThreatType) => {
            console.info("onSafeBrowsingCheckResult: [threatType]= " + threatType);
        })
    }
  }
}
```

## onScaleChange

```TypeScript
default onScaleChange(callback: Callback<OnScaleChangeEvent> | undefined): this
```

Triggered when the scale of WebView changed.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScaleChangeEvent](arkts-arkweb-web-onscalechangeevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, OnScaleChangeEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScaleChange((event: OnScaleChangeEvent) => {
          console.info('onScaleChange changed from ' + event.oldScale + ' to ' + event.newScale);
        })
    }
  }
}
```

## onScreenCaptureRequest

```TypeScript
default onScreenCaptureRequest(callback: Callback<OnScreenCaptureRequestEvent> | undefined): this
```

通知收到屏幕捕获请求。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScreenCaptureRequestEvent](arkts-arkweb-web-onscreencapturerequestevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
                  // 用户点击拒绝，调用deny通知Web组件拒绝屏幕捕获请求
                  event.handler.deny();
                }
              },
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  // 用户点击确认，调用grant通知Web组件允许屏幕捕获，并指定捕获模式为HOME_SCREEN
                  event.handler.grant({ captureMode: WebCaptureMode.HOME_SCREEN });
                }
              },
              cancel: () => {
                // 用户取消对话框，调用deny通知Web组件拒绝屏幕捕获请求
                event.handler.deny();
              }
            })
          }
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, OnScreenCaptureRequestEvent, WebCaptureMode } from '@kit.ArkUI';
import { AlertDialogParamWithButtons, AlertDialogButtonBaseOptions } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { UIContext } from "@kit.ArkUI";

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScreenCaptureRequest((event: OnScreenCaptureRequestEvent) => {
          if (event) {
            const dialogOptions: AlertDialogParamWithButtons = {
              title: 'title: ' + event.handler.getOrigin(),
              message: 'text',
              primaryButton: {
                value: 'deny',
                action: () => {
                  event.handler.deny();
                },
              } as AlertDialogButtonBaseOptions,
              secondaryButton: {
                value: 'onConfirm',
                action: () => {
                  event.handler.grant({ captureMode: WebCaptureMode.HOME_SCREEN });
                },
              } as AlertDialogButtonBaseOptions,
              cancel: () => {
                event.handler.deny();
              }
            };
            this.uiContext.showAlertDialog(dialogOptions);
          }
        })
    }
  }
}
```

## onScroll

```TypeScript
default onScroll(callback: Callback<OnScrollEvent> | undefined): this
```

Triggered when the scroll bar slides to the specified position.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnScrollEvent](arkts-arkweb-web-onscrollevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, OnScrollEvent } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onScroll((event: OnScrollEvent) => {
          console.info("x = " + event.xOffset);
          console.info("y = " + event.yOffset);
        })
    }
  }
}
```

## onSearchResultReceive

```TypeScript
default onSearchResultReceive(callback: Callback<OnSearchResultReceiveEvent> | undefined): this
```

Notify search result to host application through onSearchResultReceive.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnSearchResultReceiveEvent](arkts-arkweb-web-onsearchresultreceiveevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, OnSearchResultReceiveEvent } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onSearchResultReceive((ret: OnSearchResultReceiveEvent): void => {
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
default onShowFileSelector(callback: Callback<OnShowFileSelectorEvent, boolean> | undefined): this
```

Triggered when the file selector shows. Call this function to handle HTML forms with a "file" input type. If this function is not called or returns false, the web component provides the default "select file" handling interface. If it returns true, the application can customize the "select file" response behavior.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnShowFileSelectorEvent](arkts-arkweb-web-onshowfileselectorevent-i.md), boolean&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

拉起文件选择器。

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

拉起图库选择器。

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
    // 过滤选择媒体文件类型为IMAGE_VIDEO
    photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE;
    // 设置最大选择数量
    photoSelectOptions.maxSelectNumber = 5;
    let chooseFile: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoSelectOptions);
    // 获取选择的文件列表
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

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import { Entry, Column, Component } from '@ohos.arkui.component'
import { $rawfile, Callback, Web } from '@ohos.arkui.component'
import { UIContext } from '@ohos.arkui.UIContext'
import { webview } from '@kit.ArkWeb';
import { cameraPicker, camera } from '@kit.CameraKit';
import { BusinessError } from '@ohos.base';
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
struct Index {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件。

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
default onSslErrorEvent(callback: OnSslErrorEventCallback | undefined): this
```

Called to notify users when an SSL error occurs during the loading of resources (for the main frame and subframes). To handle SSL errors for requests for the main frame, use the isMainFrame field to distinguish.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnSslErrorEventCallback](arkts-arkweb-onsslerroreventcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
                // true表示停止加载页面，停留在当前页面，使用false表示继续加载页面，并展示错误页面
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Button, Web, Column, Component, Entry, UIContext, AlertDialogParamWithButtons, SslErrorEvent } from '@kit.ArkUI';
import { cert } from '@kit.DeviceCertificateKit';

function LogCertInfo(certChainData : Array<Uint8Array> | undefined) {
  if (!(certChainData instanceof Array)) {
    console.error('failed, cert chain data type is not array');
    return;
  }

  for (let i = 0; i < certChainData.length; i++) {
    let encodeBlobData: cert.EncodingBlob = {
      data: certChainData[i] as Uint8Array,
      encodingFormat: cert.EncodingFormat.FORMAT_DER
    }
    cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
      if (error) {
        console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
      } else {
        console.info('createX509Cert success');
        console.info(ParseX509CertInfo(x509Cert as cert.X509Cert));
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
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
          LogCertInfo(event.certChainData  as Array<Uint8Array>);
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
                // true表示停止加载页面，停留在当前页面，使用false表示继续加载页面，并展示错误页面
                event.handler.handleCancel(true);
              }
            },
            cancel: () => {
              event.handler.handleCancel();
            }
          } as AlertDialogParamWithButtons)
        })
    }
  }
}
```

## onSslErrorEventReceive

```TypeScript
default onSslErrorEventReceive(callback: Callback<OnSslErrorEventReceiveEvent> | undefined): this
```

Called to notify users when an SSL error occurs with a request for the main frame. To include errors with requests for subframes, use the OnSslErrorEvent API.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnSslErrorEventReceiveEvent](arkts-arkweb-web-onsslerroreventreceiveevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { Button, Web, Column, Component, Entry, UIContext, AlertDialogParamWithButtons, OnSslErrorEventReceiveEvent } from '@kit.ArkUI';
import { cert } from '@kit.DeviceCertificateKit';

function LogCertInfo(certChainData : Array<Uint8Array> | undefined) {
  if (!(certChainData instanceof Array)) {
    console.error('failed, cert chain data type is not array');
    return;
  }

  for (let i = 0; i < certChainData.length; i++) {
    let encodeBlobData: cert.EncodingBlob = {
      data: certChainData[i] as Uint8Array,
      encodingFormat: cert.EncodingFormat.FORMAT_DER
    } as cert.EncodingBlob
    cert.createX509Cert(encodeBlobData, (error, x509Cert) => {
      if (error) {
        console.error('Index : ' + i + ',createX509Cert failed, errCode: ' + error.code + ', errMsg: ' + error.message);
      } else {
        console.info('createX509Cert success');
        console.info(ParseX509CertInfo(x509Cert as cert.X509Cert));
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
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext = this.getUIContext();

  build() {
    Column() {
      Web({ src: 'https://example.com/', controller: this.controller })
        .onSslErrorEventReceive((event: OnSslErrorEventReceiveEvent):void => {
          LogCertInfo(event.certChainData as Array<Uint8Array>);
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
          } as AlertDialogParamWithButtons);
        })
    }
  }
}
```

## onTextSelectionChange

```TypeScript
default onTextSelectionChange(callback: TextSelectionChangeCallback | undefined): this
```

Called when the text selection changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [TextSelectionChangeCallback](arkts-arkweb-textselectionchangecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// onTextSelectionChange.ets
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, $rawfile} from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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

加载的html文件

```TypeScript
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
    <title>示例页面</title>
</head>
<body>
    示例文本
</body>
</html>
```

## onTitleReceive

```TypeScript
default onTitleReceive(callback: Callback<OnTitleReceiveEvent> | undefined): this
```

Notifies the application that the title has changed. If the page being loaded does not specify a title via the &lt;title&gt; element, ArkWeb will generate a title baseed on the URL and return it to the application.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnTitleReceiveEvent](arkts-arkweb-web-ontitlereceiveevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, OnTitleReceiveEvent } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onTitleReceive((event: OnTitleReceiveEvent): void => {
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
default onTouchIconUrlReceived(callback: Callback<OnTouchIconUrlReceivedEvent> | undefined): this
```

Triggered when the application receive the url of an apple-touch-icon.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnTouchIconUrlReceivedEvent](arkts-arkweb-web-ontouchiconurlreceivedevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, OnTouchIconUrlReceivedEvent } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'www.baidu.com', controller: this.controller })
        .onTouchIconUrlReceived((event: OnTouchIconUrlReceivedEvent): void => {
          console.info('onTouchIconUrlReceived:' + JSON.stringify(event));
        })
    }
  }
}
```

## onVerifyPin

```TypeScript
default onVerifyPin(callback: OnVerifyPinCallback | undefined): this
```

Triggered when the Web page needs verify pin from the user.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnVerifyPinCallback](arkts-arkweb-onverifypincallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import { certificateManagerDialog } from '@kit.DeviceCertificateKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController();
  uiContext : UIContext = this.getUIContext();
  context : Context | undefined = this.uiContext.getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    webview.WebviewController.setRenderProcessMode(webview.RenderProcessMode.MULTIPLE)
  }

  build() {
    Column() {
      Button('加载需要客户端SSL证书的网站')
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
          // 收到客户端证书请求事件
          console.info(`onClientAuthenticationRequest`);
          try {
            let certTypes: Array<certificateManagerDialog.CertificateType> = [
              certificateManagerDialog.CertificateType.CREDENTIAL_UKEY
            ];
            // 调用证书管理，打开证书选择框
            certificateManagerDialog.openAuthorizeDialog(this.context, { certTypes: certTypes })
              .then((data: certificateManagerDialog.CertReference) => {
                console.info(`openAuthorizeDialog request cred auth success`)
                // 通知web选择的为ukey证书
                event.handler.confirm(data.keyUri, CredentialType.CREDENTIAL_UKEY);
              }).catch((err: BusinessError) => {
              console.error(`openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(err)}`);
            })
          } catch (e) {
            console.error(`openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(e)}`);
          }
        })
        .onVerifyPin((event) => {
          // 收到PIN码认证请求事件
          console.info(`onVerifyPin`);
          // 调用证书管理，打开PIN码输入框
          certificateManagerDialog.openUkeyAuthDialog(this.context, {keyUri: event.identity})
            .then(() => {
              // 通知webPIN码认证成功
              console.info(`onVerifyPin success`);
              event.handler.confirm(PinVerifyResult.PIN_VERIFICATION_SUCCESS);
            }).catch((err: BusinessError) => {
            // 通知webPIN码认证失败
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

ArkTS-Sta示例：

```TypeScript
'use static'
import { webview } from '@kit.ArkWeb';
import { common } from '@kit.AbilityKit';
import certMgrDialog from '@ohos.security.certManagerDialog';
import { BusinessError } from '@kit.BasicServicesKit';
import { Entry, State, Component, Column, Web, Button, Context, OnClientAuthenticationEvent, OnVerifyPinCallback, VerifyPinEvent, PinVerifyResult, CredentialType, OnErrorReceiveEvent, Alignment,ClickEvent } from "@kit.ArkUI"
import { UIContext } from '@ohos.arkui.UIContext';
import { canIUse } from '@internal.full.global';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  uiContext: UIContext | null = null;
  context: Context | null = null;
  @State type: CredentialType = CredentialType.CREDENTIAL_UKEY;
  aboutToAppear(): void {
    this.uiContext = this.getUIContext();
    if (this.uiContext) {
      const hostContext = this.uiContext?.getHostContext() as common.UIAbilityContext;
      this.context = hostContext as Context;
    }
  }

  build() {
    Column() {
      Button('加载需要客户端SSL证书的网站')
        .onClick(() => {
          this.controller.loadUrl("https://client.badssl.com")
        }).height(60)
      Web({ src: "https://www.bing.com/", controller: this.controller})
        .domStorageAccess(true)
        .fileAccess(true)
        .onClientAuthenticationRequest((event:OnClientAuthenticationEvent):void => {
          // 收到客户端证书请求事件
          console.info(`RM001 onClientAuthenticationRequest`);
          if (!this.context) {
            console.error(`RM001 The context is not initialized`);
          }
          const nonNullContext = this.context!;
          try {
            let certTypes: Array<certMgrDialog.CertificateType> = [
              certMgrDialog.CertificateType.CREDENTIAL_UKEY
            ];
            // 调用证书管理，打开证书选择框
            certMgrDialog.openAuthorizeDialog(nonNullContext, { certTypes: certTypes })
              .then((data: certMgrDialog.CertReference) => {
                console.info(`RM001 openAuthorizeDialog request cred auth success`)
                // 通知web选择的为ukey证书
                event.handler.confirm(data.keyUri, CredentialType.CREDENTIAL_UKEY);
              }).catch((err): void => {
              console.error(`RM001 openAuthorizeDialog request cred auth failed, err.code:${err.code},err.message:${err.message}`);
            })
          } catch (e) {
            console.error(`RM001 openAuthorizeDialog request cred auth failed, err: ${JSON.stringify(e)}`);
          }
        })
        .onVerifyPin((event:VerifyPinEvent):void => {
          // 收到PIN码认证请求事件
          console.info('RM001 onVerifyPin')
          if (!this.context) {
            console.error(`RM001 The context is not initialized`);
            return;
          }
          const nonNullContext = this.context!;
          // 调用证书管理，打开PIN码输入框
          certMgrDialog.openUkeyAuthDialog(nonNullContext, {keyUri: event.identity})
            .then(() => {
              // 通知webPIN码认证成功
              console.info('RM001 onVerifyPin success');
              event.handler.confirm(PinVerifyResult.PIN_VERIFICATION_SUCCESS);
            }).catch((err):void => {
            // 通知webPIN码认证失败
            console.info('RM001 onVerifyPin fail');
            event.handler.confirm(PinVerifyResult.PIN_VERIFICATION_FAILED);
          })
        })
        .onErrorReceive((event:OnErrorReceiveEvent) => {
          if (event) {
            this.getUIContext().getPromptAction().showToast({
              message: `ErrorCode: ${event.error.getErrorCode()}, ErrorInfo: ${event.error.getErrorInfo()}`,
              alignment: Alignment.Center
            })
            console.info('RM001 getErrorInfo:' + event.error.getErrorInfo());
            console.info('RM001 getErrorCode:' + event.error.getErrorCode());
            console.info('RM001 url:' + event.request.getRequestUrl());
          }
        })
        .onTitleReceive(event  => {
          console.info("RM001 title received " + event.title);
        })

    }
  }
}
```

## onViewportFitChanged

```TypeScript
default onViewportFitChanged(callback: OnViewportFitChangedCallback | undefined): this
```

Called when the viewport-fit configuration in the web page's &lt;meta&gt; tag changes. The application can adapt its layout to the viewport within this callback.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [OnViewportFitChangedCallback](arkts-arkweb-onviewportfitchangedcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
            // index.html网页支持沉浸式布局，可调用expandSafeArea调整web控件布局视口覆盖避让区域(状态栏或导航条)。
          } else if (viewportFit === ViewportFit.CONTAINS) {
            // index.html网页不支持沉浸式布局，可调用expandSafeArea调整web控件布局视口为安全区域。
          } else {
            // 默认值，可不作处理。
          }
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Entry, Component, Web, Column, ViewportFit } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

build() {
  Column() {
    Web({ src: $rawfile('index.html'), controller: this.controller })
      .onViewportFitChanged((data:ViewportFit):void => {
        console.info("data:",data)
        if (data === ViewportFit.COVER) {
          // index.html网页支持沉浸式布局，可调用expandSafeArea调整web控件布局视口覆盖避让区域(状态栏或导航条)。
        } else if (data === ViewportFit.CONTAINS) {
          // index.html网页不支持沉浸式布局，可调用expandSafeArea调整web控件布局视口为安全区域。
        } else {
          // 默认值，可不作处理。
        }
      })
    }
  }
}
```

加载的html文件。

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
default onWindowExit(callback: (() => void) | undefined): this
```

Notifies the user of the window closing request. Like [onWindowNew](#onwindownew), from a security perspective, applications should ensure that users can know that the page they interact with is closed.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (() = & gt; void) \ | undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default onWindowNew(callback: Callback<OnWindowNewEvent> | undefined): this
```

Triggered when web page requires the user to create a window. If the [setWebController](arkts-arkweb-web-controllerhandler-c.md#setwebcontroller) interface is not called, the render process will be blocked. If no new window is created, it is set to null when calling the [setWebController](arkts-arkweb-web-controllerhandler-c.md#setwebcontroller) interface, informing the Web that no new window is created. The new window should avoid being directly overlaid on the original Web component, and its URL (such as address bar) should be clearly displayed in the same form as the main page to prevent users from being confused. If credible URL visualization management cannot be achieved, it is necessary to consider prohibiting the creation of new windows. It should be noted that the source of the new window request cannot be traced reliably, and it may be initiated by a third party iframe. The application needs to take defensive measures such as sandbox isolation and permission restriction by default to ensure security.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnWindowNewEvent](arkts-arkweb-web-onwindownewevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

// 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
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
        // 需要使能multiWindowAccess。
        .multiWindowAccess(true)
        .allowWindowOpenMethod(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController.close();
          }
          let popController: webview.WebviewController = new webview.WebviewController();
          // 将新窗口对应WebviewController返回给Web内核。
          // 若不调用event.handler.setWebController接口，会造成渲染进程阻塞。
          // 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
          event.handler.setWebController(popController);
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController })
          })
          this.dialogController.open();
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Component, Entry, Web, Column, CustomDialogController, CustomDialog } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

// 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
@CustomDialog
struct NewWebViewComp {
  controller?: CustomDialogController;
  webviewController1: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: "www.example.com", controller: this.webviewController1 })
        .javaScriptAccess(true)
        .multiWindowAccess(false)
        .onWindowExit(() => {
          console.info("NewWebViewComp onWindowExit");
          if (this.controller) {
            this.controller?.close();
          }
        })
    }
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  dialogController: CustomDialogController | null = null;

  build() {
    Column() {
      Web({ src: $rawfile("window.html"), controller: this.controller })
        .javaScriptAccess(true)
        // 需要使能multiWindowAccess。
        .multiWindowAccess(true)
        .allowWindowOpenMethod(true)
        .onWindowNew((event) => {
          if (this.dialogController) {
            this.dialogController?.close();
          }
          let popController: webview.WebviewController = new webview.WebviewController(undefined);
          // 将新窗口对应WebviewController返回给Web内核。
          // 若不调用event.handler.setWebController接口，会造成渲染进程阻塞。
          // 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
          event.handler.setWebController(popController);
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController })
          })
          this.dialogController?.open();
        })
    }
  }
}
```

```TypeScript
<!-- window.html页面代码 -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
<a href="#" onclick="openNewWindow('https://www.example.com')">打开新页面</a>
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
default onWindowNewExt(callback: Callback<OnWindowNewExtEvent> | undefined): this
```

Triggered when web page requires the user to create a window. If the [setWebController](arkts-arkweb-web-controllerhandler-c.md#setwebcontroller) interface is not called, the render process will be blocked. If no new window is created, it is set to null when calling the [setWebController](arkts-arkweb-web-controllerhandler-c.md#setwebcontroller) interface, informing the Web that no new window is created. The new window should avoid being directly overlaid on the original Web component, and its URL (such as address bar) should be clearly displayed in the same form as the main page to prevent users from being confused. If credible URL visualization management cannot be achieved, it is necessary to consider prohibiting the creation of new windows. It should be noted that the source of the new window request cannot be traced reliably, and it may be initiated by a third party iframe. The application needs to take defensive measures such as sandbox isolation and permission restriction by default to ensure security.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;[OnWindowNewExtEvent](arkts-arkweb-web-onwindownewextevent-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';

// 在同一page页有两个Web组件。在WebComponent新开窗口时，会跳转到NewWebViewComp。
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
      // 需要开启multiWindowAccess
      .multiWindowAccess(true)
      .allowWindowOpenMethod(true)
      .onWindowNewExt((event) => {
        // 以event.navigationPolicy请求的方式打开新窗口
        console.info("navigationAction: ", event.navigationPolicy)
        // 以event.windowFeatures中的大小及位置信息创建新窗口
        console.info("windowFeatures: ", JSON.stringify(event.windowFeatures))
        if (this.dialogController) {
          this.dialogController.close();
        }
        let popController: webview.WebviewController = new webview.WebviewController();
        // 将新窗口对应WebviewController返回给Web内核。
        // 若不调用event.handler.setWebController接口，会造成渲染进程阻塞。
        // 如果没有创建新窗口，在调用event.handler.setWebController接口时应设置成null，以通知Web没有创建新窗口。
        event.handler.setWebController(popController);
        this.dialogController = new CustomDialogController({
          builder: NewWebViewComp({ webviewController1: popController })
        })
        this.dialogController.open();
      })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'

// xxx.ets
import { $rawfile, Component, Entry, Web, Column, CustomDialogController, CustomDialog, OnWindowNewExtEvent } from "@ohos.arkui.component";
import webview  from '@ohos.web.webview';

@CustomDialog
struct NewWebViewComp {
  controller?: CustomDialogController;
  webviewController1: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: "www.example.com", controller: this.webviewController1 })
        .javaScriptAccess(true)
        .multiWindowAccess(true)
        .allowWindowOpenMethod(true)
        .onWindowExit(() => {
          console.info("NewWebViewComp onWindowExit");
          if (this.controller) {
            this.controller?.close();
          }
        })
    }
  }
}


@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  dialogController: CustomDialogController | null = null;

  build() {
    Column() {
      Web({ src: "resource://rawfile/window.html", controller: this.controller })
        .javaScriptAccess(true)
        .multiWindowAccess(true)
        .allowWindowOpenMethod(true)
        .onWindowNewExt((event:OnWindowNewExtEvent):void => {
          //以event.navigationPolicy请求的方式打开新窗口
          console.info("navigationAction: ", event.navigationPolicy)
          //以event.windowFeatures中的大小及位置信息创建新窗口
          console.info("windowFeatures: ", JSON.stringify(event.windowFeatures))

          if (this.dialogController) {
            this.dialogController?.close();
          }

          let popController: webview.WebviewController = new webview.WebviewController(undefined);
          // 将新窗口对应WebviewController返回给Web内核。
          // 若不调用event.handler.setWebController接口，会造成渲染进程阻塞。
          // 如果没有创建新窗口，调用event.handler.setWebController接口时设置成null，通知Web没有创建新窗口。
          event.handler.setWebController(popController);
          this.dialogController = new CustomDialogController({
            builder: NewWebViewComp({ webviewController1: popController })
          })
          this.dialogController?.open();
        })
    }
  }
}
```

```TypeScript
<!-- window.html页面代码 -->
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
  <a href="#" onclick="openNewWindow('https://www.example.com')">打开新页面</a>
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
default optimizeParserBudget(optimizeParserBudget: boolean | undefined): this
```

Sets whether to optimize parser budget to reduce FCP time

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [optimizeParserBudget](#optimizeparserbudget) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry } from '@kit.ArkUI';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined)
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
default overScrollMode(mode: OverScrollMode | undefined): this
```

Sets the over-scroll mode for web When the scrolling mode is enabled, when the user slides to the edge on the web root page, the web will bounce back the interface through elastic animation, and the internal pages on the root page will not trigger the bounce back.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [OverScrollMode](arkts-arkweb-web-overscrollmode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, State, OverScrollMode } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default overviewModeAccess(overviewModeAccess: boolean | undefined): this
```

Sets whether to load web pages by using the overview mode, which means reducing the content to fit the screen width. Currently, only mobile devices are supported.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [overviewModeAccess](#overviewmodeaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default pinchSmooth(isEnabled: boolean | undefined): this
```

Sets whether to enable smooth pinch mode for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isEnabled | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default registerNativeEmbedRule(tag: string | undefined, type: string | undefined): this
```

Registers the HTML tag name and type for same-layer rendering. The tag name only supports object and embed. The tag type only supports visible ASCII characters.<br> If the specified type is the same as the W3C standard object or embed type, the ArkWeb kernel identifies the type as a non-same-layer tag.<br> This API is also controlled by the enableNativeEmbedMode API and does not take effect if same-layer rendering is not enabled. When this API is not used, the ArkWeb kernel recognizes the embed tags with the "native/" prefix as same-layer tags.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tag | string \| undefined | 是 |
| type | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
           // 配置同层渲染开关开启。
          .enableNativeEmbedMode(true)
           // 注册同层标签为<object>，类型为"native"前缀。
          .registerNativeEmbedRule("object", "native")
           // 获取<object>标签的生命周期变化数据。
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'

import { webview } from '@kit.ArkWeb';
import { UIContext, $rawfile, Entry, Component, Web, Column, Button, State,
  TouchEvent, NodeController, BuilderNode, NodeRenderType, PropRef, FrameNode,
  Color, Stack, NodeContainer, NativeEmbedStatus, NativeEmbedDataInfo, wrapBuilder } from '@kit.ArkUI';

export class Params {
  text: string = '';
  width: double = 0;
  height: double = 0;
}

export class NodeControllerParams {
  surfaceId: string = '';
  renderType: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  width: double = 0;
  height: double = 0;
}

export class MyNodeController extends NodeController {
  private rootNode: BuilderNode<Params> | undefined | null;
  private surfaceId_: string = "";
  private renderType_: NodeRenderType = NodeRenderType.RENDER_TYPE_DISPLAY;
  private width_: double = 0;
  private height_: double = 0;

  setRenderOption(params: NodeControllerParams) {
    this.surfaceId_ = params.surfaceId;
    this.renderType_ = params.renderType;
    this.width_ = params.width;
    this.height_ = params.height;
  }

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode<Params>(uiContext, { surfaceId: this.surfaceId_, type: this.renderType_ });
    this.rootNode?.build(wrapBuilder(ButtonBuilder), { text: "myButton", width: this.width_, height: this.height_ });
    return this.rootNode?.getFrameNode() ?? null;
  }

  postInputEvent(event: TouchEvent): boolean {
    return this.rootNode?.postInputEvent(event) as boolean;
  }
}

@Component
struct ButtonComponent {
  @PropRef params: Params;
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
           // 配置同层渲染开关开启。
          .enableNativeEmbedMode(true)
           // 注册同层标签为<object>，类型为"native"前缀。
          .registerNativeEmbedRule("object", "native")
           // 获取<object>标签的生命周期变化数据。
          .onNativeEmbedLifecycleChange((object: NativeEmbedDataInfo):void => {
            if (object.status == NativeEmbedStatus.CREATE) {
              this.nodeController.setRenderOption({
                surfaceId: object.surfaceId as string,
                renderType: NodeRenderType.RENDER_TYPE_TEXTURE,
                width: this.uiContext!.px2vp(object.info?.width as int),
                height: this.uiContext!.px2vp(object.info?.height as int)
              } as NodeControllerParams);
              this.nodeController.rebuild();
            }
          })
      }
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
    <title>同层渲染测试</title>
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
default rotateRenderEffect(effect: WebRotateEffect | undefined): this
```

Set up the effect of web rotation

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [WebRotateEffect](arkts-arkweb-web-webrotateeffect-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Column, Component, Web, WebRotateEffect } from '@ohos.arkui.component'
import { State } from '@ohos.arkui.stateManagement';
import webview from '@ohos.web.webview';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State effect: WebRotateEffect = WebRotateEffect.TOPLEFT_EFFECT;
  build() {
    Column() {
      Web({ src: 'resource://rawfile/index.html', controller: this.controller })
        .rotateRenderEffect(this.effect)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <title>测试网页</title>
</head>
<body>
  <p>测试网页</p>
</body>
</html>
```

## runJavaScriptOnDocumentEnd

```TypeScript
default runJavaScriptOnDocumentEnd(scripts: Array<ScriptItem> | undefined): this
```

Injects the JavaScripts that will be run after document has been parsed finished.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-web-scriptitem-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, State, ScriptItem, $rawfile, Color } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  private jsStr: string =
    "window.document.getElementById(\"result\").innerHTML = 'this is msg from runJavaScriptOnDocumentEnd'";
  @State scripts: Array<ScriptItem> = [
    { script: this.jsStr, scriptRules: ["*"] } as ScriptItem
  ];

  build() {
    Column() {
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
default runJavaScriptOnDocumentStart(scripts: Array<ScriptItem> | undefined): this
```

Injects the JavaScripts that will be run just after document object has been created.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-web-scriptitem-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

## runJavaScriptOnHeadEnd

```TypeScript
default runJavaScriptOnHeadEnd(scripts: Array<ScriptItem> | undefined): this
```

Injects the JavaScripts that will be run after head element has been parsed finished.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| scripts | Array&lt;[ScriptItem](arkts-arkweb-web-scriptitem-i.md)&gt; \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { webview } from '@kit.ArkWeb';
import { Web, Column, Component, Entry, State, ScriptItem, $rawfile, Color } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  private jsStr: string =
    "window.document.getElementById(\"result\").innerHTML = 'this is msg from runJavaScriptOnHeadEnd'";
  private jsStr2: string = "console.info('runJavaScriptOnHeadEnd urlRegexRules Matching succeeded.')";
  @State scripts: Array<ScriptItem> = [
    { script: this.jsStr, scriptRules: ["*"] } as ScriptItem,
    { script: this.jsStr2, scriptRules: [], urlRegexRules: [{secondLevelDomain: "", rule: ".*index.html"}] } as ScriptItem
  ];

  build() {
    Column() {
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
default scrollbarLayoutPolicy(policy: ScrollbarLayoutPolicy | undefined): this
```

Sets the scrollbar layout policy.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policy | [ScrollbarLayoutPolicy](arkts-arkweb-web-scrollbarlayoutpolicy-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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
        // 设置为SYSTEM表示跟随系统语言方向布局。设置为CONTENT表示沿用Web样式布局
        .scrollbarLayoutPolicy(ScrollbarLayoutPolicy.SYSTEM)
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, $rawfile, ScrollbarLayoutPolicy } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: $rawfile("index.html"), controller: this.controller })
        .width('100%')
        .height('100%')
        // 设置为SYSTEM表示跟随系统语言方向布局。设置为CONTENT表示沿用Web样式布局
        .scrollbarLayoutPolicy(ScrollbarLayoutPolicy.SYSTEM)
    }
  }
}
```

加载的html文件。

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

## textAutosizing

```TypeScript
default textAutosizing(textAutosizing: boolean | undefined): this
```

Sets whether automatic text resizing is enabled. After the automatic text font size adjustment takes effect, the font size will be automatically increased to 16px~32px for text with too small font size to avoid the readability problem of small fonts due to the lack of mobile adaptation for devices with small screens (default viewport width &lt; 980px).<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> Prerequisites for the automatic adjustment of text font size to take effect: 1.The device forms are: Phone, Tablet, Wearable, TV. 2.Web component viewport width &lt; 980px. 3.The page text is large, and the font size * number of characters of the page text is ≥ 3920. 4.There is no metaViewport setting on the frontend, or no "width" and "initial-scale" attributes in the metaViewport setting.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [textAutosizing](#textautosizing) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default textZoomRatio(textZoomRatio: int | undefined): this
```

Sets the ratio of the text zoom.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [textZoomRatio](#textzoomratio) | int \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State ratio: int = 150;

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
default verticalScrollBarAccess(verticalScrollBar: boolean | undefined): this
```

Set whether paint vertical scroll bar, including the system default scrollbar and user-defined scrollbar.<p>&lt;strong&gt;API Note&lt;/strong&gt;:<br> After controlling the vertical scrollbar's visibility through the @State variable, you need to call controller.refresh() to take effect.<br> When frequently changing the @State variable dynamically, it is recommended to match the toggle variable with the Web component one-to-one. </p>

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| verticalScrollBar | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State isShow: boolean = true;
  @State btnMsg: string = '隐藏滚动条';

  build() {
    Column() {
      // 通过@State变量改变纵向滚动条的隐藏/显示后，需调用this.controller.refresh()后生效
      Button(this.btnMsg)
        .onClick(() => {
          if (this.isShow) {
            this.isShow = false;
            this.btnMsg = '显示滚动条';
          } else {
            this.isShow = true;
            this.btnMsg = '隐藏滚动条';
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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Column, Component, Entry, State, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);
  @State isShow: boolean = true;
  @State btnMsg: string = '隐藏滚动条';

  build() {
    Column() {
      // 通过@State变量改变纵向滚动条的隐藏/显示后，需调用this.controller.refresh()后生效。
      Button(this.btnMsg)
        .onClick((): void => {
          if (this.isShow) {
            this.isShow = false;
            this.btnMsg = '隐藏滚动条';
          } else {
            this.isShow = true;
            this.btnMsg = '显示滚动条';
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

加载的html文件。

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
default webCursiveFont(family: string | undefined): this
```

Sets the cursive font family for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| family | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default webFantasyFont(family: string | undefined): this
```

Sets the fantasy font family for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| family | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default webFixedFont(family: string | undefined): this
```

Sets the fixed font family for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| family | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default webSansSerifFont(family: string | undefined): this
```

Sets the sans serif font family for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| family | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default webSerifFont(family: string | undefined): this
```

Sets a serif font family for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| family | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { State, Entry, Column, Component, Web } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default webStandardFont(family: string | undefined): this
```

Sets the standard font family for the web page.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| family | string \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Entry, Component, Web, Column, State } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
controller: webview.WebviewController = new webview.WebviewController(undefined);
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
default zoomAccess(zoomAccess: boolean | undefined): this
```

Sets whether the Web supports zooming using gestures.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [zoomAccess](#zoomaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { Web, Column, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

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
default zoomControlAccess(zoomControlAccess: boolean | undefined): this
```

Sets whether the Web supports zooming using Ctrl.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [zoomControlAccess](#zoomcontrolaccess) | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [WebAttribute](arkts-arkweb-web-webattribute-i.md) |

**示例**

ArkTS-Dyn示例：

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

ArkTS-Sta示例：

```TypeScript
// xxx.ets
import { Entry, Column, Component, Web } from '@ohos.arkui.component'
import webview from '@ohos.web.webview';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Web({ src: 'resource://rawfile/index.html', controller: this.controller })
        .zoomControlAccess(true)
    }
  }
}
```

加载的html文件。

```TypeScript
<!--index.html-->
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>测试网页</title>
</head>
<body>
  <h1>zoomControlAccess Demo</h1>
  <span>You can zoom in/out page when zoomControlAccess is true.</span>
</body>
</html>
```
