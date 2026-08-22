# WebSchemeHandlerResponse

Defines the Web resource response used for scheme handler.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-class WebSchemeHandlerResponse--><!--Device-webview-class WebSchemeHandlerResponse-End-->

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-constructor()--><!--Device-WebSchemeHandlerResponse-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Examples**

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
  controller: webview.WebviewController = new webview.WebviewController()
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

HTML file to be loaded:

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

## getCustomErrorCode

```TypeScript
getCustomErrorCode(): int
```

Get the custom error code of the Web response.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSchemeHandlerResponse-getCustomErrorCode(): int--><!--Device-WebSchemeHandlerResponse-getCustomErrorCode(): int-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Return the custom error code that was set for this response. |

## getEncoding

```TypeScript
getEncoding(): string
```

Get the response encoding.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-getEncoding(): string--><!--Device-WebSchemeHandlerResponse-getEncoding(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return encoding of response. |

## getHeaderByName

```TypeScript
getHeaderByName(name: string): string
```

Get the header value by name from the response.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-getHeaderByName(name: string): string--><!--Device-WebSchemeHandlerResponse-getHeaderByName(name: string): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Header name. |

**Return value:**

| Type | Description |
| --- | --- |
| string | Return header value by name. |

## getMimeType

```TypeScript
getMimeType(): string
```

Get mime type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-getMimeType(): string--><!--Device-WebSchemeHandlerResponse-getMimeType(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return mime type of response. |

## getNetErrorCode

```TypeScript
getNetErrorCode(): WebNetErrorList
```

Get net error code.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-getNetErrorCode(): WebNetErrorList--><!--Device-WebSchemeHandlerResponse-getNetErrorCode(): WebNetErrorList-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| [WebNetErrorList](../../apis-arkweb/arkts-apis/arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | Return response error code. |

## getStatus

```TypeScript
getStatus(): int
```

Get http status code.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-getStatus(): int--><!--Device-WebSchemeHandlerResponse-getStatus(): int-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| int | Return http status code. |

## getStatusText

```TypeScript
getStatusText(): string
```

Get status text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-getStatusText(): string--><!--Device-WebSchemeHandlerResponse-getStatusText(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return http status text. |

## getUrl

```TypeScript
getUrl(): string
```

Get the resolved URL after redirects or changed as a result of HSTS.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-getUrl(): string--><!--Device-WebSchemeHandlerResponse-getUrl(): string-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Return value:**

| Type | Description |
| --- | --- |
| string | Return response url for redirects. |

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

## setCustomErrorCode

```TypeScript
setCustomErrorCode(customErrorCode: int): void
```

Set the custom error code for the Web response.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebSchemeHandlerResponse-setCustomErrorCode(customErrorCode: int): void--><!--Device-WebSchemeHandlerResponse-setCustomErrorCode(customErrorCode: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| customErrorCode | int | Yes | The custom error code for this response, Web engine will pass the custom error code directly to the application through onErrorReceive. <br>The value should be an integer. |

## setEncoding

```TypeScript
setEncoding(encoding: string): void
```

Set the response encoding.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-setEncoding(encoding: string): void--><!--Device-WebSchemeHandlerResponse-setEncoding(encoding: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| encoding | string | Yes | Encoding. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setHeaderByName

```TypeScript
setHeaderByName(name: string, value: string, overwrite: boolean): void
```

Set response hander value by name.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-setHeaderByName(name: string, value: string, overwrite: boolean): void--><!--Device-WebSchemeHandlerResponse-setHeaderByName(name: string, value: string, overwrite: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Header name. |
| value | string | Yes | Header value. |
| overwrite | boolean | Yes | Whether to overwrite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

## setMimeType

```TypeScript
setMimeType(type: string): void
```

Set mime type.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-setMimeType(type: string): void--><!--Device-WebSchemeHandlerResponse-setMimeType(type: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Mime type. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setNetErrorCode

```TypeScript
setNetErrorCode(code: WebNetErrorList): void
```

Set net error code.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-setNetErrorCode(code: WebNetErrorList): void--><!--Device-WebSchemeHandlerResponse-setNetErrorCode(code: WebNetErrorList): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | [WebNetErrorList](../../apis-arkweb/arkts-apis/arkts-arkweb-web-neterrorlist-webneterrorlist-e.md) | Yes | Set net error code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. |

## setStatus

```TypeScript
setStatus(code: int): void
```

Set http status code.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-setStatus(code: int): void--><!--Device-WebSchemeHandlerResponse-setStatus(code: int): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| code | int | Yes | Http status code. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setStatusText

```TypeScript
setStatusText(text: string): void
```

Set status text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-setStatusText(text: string): void--><!--Device-WebSchemeHandlerResponse-setStatusText(text: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Status text. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## setUrl

```TypeScript
setUrl(url: string): void
```

Set the resolved URL after redirects or changed as a result of HSTS.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebSchemeHandlerResponse-setUrl(url: string): void--><!--Device-WebSchemeHandlerResponse-setUrl(url: string): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| url | string | Yes | Set response url for redirects. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |

