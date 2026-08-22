# WebSchemeHandlerResponse

Defines the Web resource response used for scheme handler.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-webview-class WebSchemeHandlerResponse--><!--Device-webview-class WebSchemeHandlerResponse-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructor.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-constructor()--><!--Device-WebSchemeHandlerResponse-constructor()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**示例**

ArkTS-Dyn示例：

```TypeScript
// xxx.ets
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class WebObj {
  constructor() {
  }

  webTest(): string {
    console.info('Web test');
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString');
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();
  @State webTestObj: WebObj = new WebObj();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objTestName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: '', controller: this.controller })
        .javaScriptAccess(true)
        .onControllerAttached(() => {
          this.controller.loadUrl($rawfile("index.html"));
          this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
        })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
// xxx.ets
'use static'
import { $rawfile, Web, Button, Column, State, Component, Entry } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@kit.BasicServicesKit';

class WebObj {
  constructor() {
  }

  webTest(): string {
    console.info('Web test');
    return "Web test";
  }

  webString(): void {
    console.info('Web test toString');
  }
}

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined)
  @State webTestObj: WebObj = new WebObj();

  build() {
    Column() {
      Button('refresh')
        .onClick(() => {
          try {
            this.controller.refresh();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Button('deleteJavaScriptRegister')
        .onClick(() => {
          try {
            this.controller.deleteJavaScriptRegister("objTestName");
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: '', controller: this.controller })
        .javaScriptAccess(true)
        .onControllerAttached(() => {
          this.controller.loadUrl($rawfile("index.html"));
          this.controller.registerJavaScriptProxy(this.webTestObj, "objTestName", ["webTest", "webString"]);
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
      <button type="button" onclick="htmlTest()">Click Me!</button>
      <p id="demo"></p>
      <p id="webDemo"></p>
      <script type="text/javascript">
        function htmlTest() {
          // This function call expects to return "Web test"
          let webStr = objTestName.webTest();
          document.getElementById("webDemo").innerHTML=webStr;
          console.info('objTestName.webTest result:'+ webStr)
        }
      </script>
    </body>
</html>
```

## getEncoding

```TypeScript
getEncoding(): string
```

Get the response encoding.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-getEncoding(): string--><!--Device-WebSchemeHandlerResponse-getEncoding(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return encoding of response. |

## getHeaderByName

```TypeScript
getHeaderByName(name: string): string
```

Get the header value by name from the response.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-getHeaderByName(name: string): string--><!--Device-WebSchemeHandlerResponse-getHeaderByName(name: string): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | Header name. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return header value by name. |

## getMimeType

```TypeScript
getMimeType(): string
```

Get mime type.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-getMimeType(): string--><!--Device-WebSchemeHandlerResponse-getMimeType(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return mime type of response. |

## getNetErrorCode

```TypeScript
getNetErrorCode(): WebNetErrorList
```

Get net error code.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-getNetErrorCode(): WebNetErrorList--><!--Device-WebSchemeHandlerResponse-getNetErrorCode(): WebNetErrorList-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebNetErrorList](../../apis-arkweb/arkts-apis/arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | Return response error code. |

## getStatus

```TypeScript
getStatus(): int
```

Get http status code.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-getStatus(): int--><!--Device-WebSchemeHandlerResponse-getStatus(): int-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| int | Return http status code. |

## getStatusText

```TypeScript
getStatusText(): string
```

Get status text.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-getStatusText(): string--><!--Device-WebSchemeHandlerResponse-getStatusText(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return http status text. |

## getUrl

```TypeScript
getUrl(): string
```

Get the resolved URL after redirects or changed as a result of HSTS.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-getUrl(): string--><!--Device-WebSchemeHandlerResponse-getUrl(): string-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Return response url for redirects. |

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
      Button('getUrl')
        .onClick(() => {
          try {
            let url = this.controller.getUrl();
            console.info("url: " + url);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

ArkTS-Sta示例：

```TypeScript
'use static'
import { Web, Column, Component, Entry, Button } from '@kit.ArkUI';
import { webview } from '@kit.ArkWeb';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController(undefined);

  build() {
    Column() {
      Button('getUrl')
        .onClick(() => {
          try {
            let url = this.controller.getUrl();
            console.info("url: " + url);
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}`);
          }
        })
      Web({ src: 'www.example.com', controller: this.controller })
    }
  }
}
```

## setEncoding

```TypeScript
setEncoding(encoding: string): void
```

Set the response encoding.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-setEncoding(encoding: string): void--><!--Device-WebSchemeHandlerResponse-setEncoding(encoding: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| encoding | string | 是 | Encoding. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setHeaderByName

```TypeScript
setHeaderByName(name: string, value: string, overwrite: boolean): void
```

Set response hander value by name.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-setHeaderByName(name: string, value: string, overwrite: boolean): void--><!--Device-WebSchemeHandlerResponse-setHeaderByName(name: string, value: string, overwrite: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | Header name. |
| value | string | 是 | Header value. |
| overwrite | boolean | 是 | Whether to overwrite. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

## setMimeType

```TypeScript
setMimeType(type: string): void
```

Set mime type.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-setMimeType(type: string): void--><!--Device-WebSchemeHandlerResponse-setMimeType(type: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | Mime type. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setNetErrorCode

```TypeScript
setNetErrorCode(code: WebNetErrorList): void
```

Set net error code.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-setNetErrorCode(code: WebNetErrorList): void--><!--Device-WebSchemeHandlerResponse-setNetErrorCode(code: WebNetErrorList): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | [WebNetErrorList](../../apis-arkweb/arkts-apis/arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | 是 | Set net error code. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

## setStatus

```TypeScript
setStatus(code: int): void
```

Set http status code.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-setStatus(code: int): void--><!--Device-WebSchemeHandlerResponse-setStatus(code: int): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | int | 是 | Http status code. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setStatusText

```TypeScript
setStatusText(text: string): void
```

Set status text.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-setStatusText(text: string): void--><!--Device-WebSchemeHandlerResponse-setStatusText(text: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | Status text. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setUrl

```TypeScript
setUrl(url: string): void
```

Set the resolved URL after redirects or changed as a result of HSTS.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-WebSchemeHandlerResponse-setUrl(url: string): void--><!--Device-WebSchemeHandlerResponse-setUrl(url: string): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| url | string | 是 | Set response url for redirects. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [401](../../errorcode-universal.md#401-参数检查失败) | Parameter error. Possible causes: 1. Incorrect parameter types. |

