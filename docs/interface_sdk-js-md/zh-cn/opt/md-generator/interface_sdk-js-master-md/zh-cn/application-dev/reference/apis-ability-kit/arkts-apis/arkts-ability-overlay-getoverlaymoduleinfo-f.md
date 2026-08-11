# getOverlayModuleInfo

## getOverlayModuleInfo

```TypeScript
function getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void
```

获取当前应用中overlay特征module的OverlayModuleInfo信息。使用callback异步回调。

**起始版本：** 10

<!--Device-overlay-function getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void--><!--Device-overlay-function getOverlayModuleInfo(moduleName: string, callback: AsyncCallback<OverlayModuleInfo>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;OverlayModuleInfo&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700032](../errorcode-bundle.md#17700032-指定的应用不包含overlay特征的module) |
| [17700033](../errorcode-bundle.md#17700033-指定的module不是overlay特征的module) |

## 示例

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";

try {
  overlay.getOverlayModuleInfo(moduleName, (err, data) => {
    if (err) {
      console.error('getOverlayModuleInfo failed due to err code : ' + err.code + ' ' + 'message :' + err.message);
      return;
    }
    console.info('overlayModuleInfo is ' + JSON.stringify(data));
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
}
```


## getOverlayModuleInfo

```TypeScript
function getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>
```

获取当前应用中overlay特征module的OverlayModuleInfo信息。使用Promise异步回调。

**起始版本：** 10

<!--Device-overlay-function getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>--><!--Device-overlay-function getOverlayModuleInfo(moduleName: string): Promise<OverlayModuleInfo>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| moduleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;OverlayModuleInfo&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700032](../errorcode-bundle.md#17700032-指定的应用不包含overlay特征的module) |
| [17700033](../errorcode-bundle.md#17700033-指定的module不是overlay特征的module) |

## 示例

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let moduleName = "feature";

(async () => {
  try {
    let overlayModuleInfo = await overlay.getOverlayModuleInfo(moduleName);
    console.info('overlayModuleInfo is ' + JSON.stringify(overlayModuleInfo));
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error('getOverlayModuleInfo failed due to err code : ' + code + ' ' + 'message :' + message);
  }
})();
```
