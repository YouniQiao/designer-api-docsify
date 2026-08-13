# getTargetOverlayModuleInfosByBundleName（系统接口）

## getTargetOverlayModuleInfosByBundleName

```TypeScript
function getTargetOverlayModuleInfosByBundleName(targetBundleName: string,
      callback: AsyncCallback<Array<OverlayModuleInfo>>): void
```

获取指定应用中所有module关联的所有OverlayModuleInfo信息。使用callback异步回调。 指定应用是调用方自身时不需要权限。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-overlay-function getTargetOverlayModuleInfosByBundleName(targetBundleName: string,      callback: AsyncCallback<Array<OverlayModuleInfo>>): void--><!--Device-overlay-function getTargetOverlayModuleInfosByBundleName(targetBundleName: string,      callback: AsyncCallback<Array<OverlayModuleInfo>>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetBundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;OverlayModuleInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700035](../errorcode-bundle.md#17700035-指定的应用只包含overlay特征的module) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetBundleName = "com.example.myapplication_xxxxx";

try {
  overlay.getTargetOverlayModuleInfosByBundleName(targetBundleName, (err, data) => {
    if (err) {
      console.error('getTargetOverlayModuleInfosByBundleName failed due to err code : ' + err.code + ' ' + 'message :' +
      err.message);
      return;
    }
    console.info('overlayModuleInfo is ' + JSON.stringify(data));
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('getTargetOverlayModuleInfosByBundleName failed due to err code : ' + code + ' ' + 'message :' +
    message);
}
```


## getTargetOverlayModuleInfosByBundleName

```TypeScript
function getTargetOverlayModuleInfosByBundleName(targetBundleName: string, moduleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void
```

获取指定应用中指定module关联的所有OverlayModuleInfo信息。使用callback异步回调。 指定应用是调用方自身时不需要权限。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-overlay-function getTargetOverlayModuleInfosByBundleName(targetBundleName: string, moduleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void--><!--Device-overlay-function getTargetOverlayModuleInfosByBundleName(targetBundleName: string, moduleName: string, callback: AsyncCallback<Array<OverlayModuleInfo>>): void-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetBundleName | string | 是 |
| moduleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;OverlayModuleInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700034](../errorcode-bundle.md#17700034-指定的module是overlay特征的module) |
| [17700035](../errorcode-bundle.md#17700035-指定的应用只包含overlay特征的module) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetBundleName = "com.example.myapplication_xxxxx";
let moduleName = "feature";

try {
  overlay.getTargetOverlayModuleInfosByBundleName(targetBundleName, moduleName, (err, data) => {
    if (err) {
      console.error('getTargetOverlayModuleInfosByBundleName failed due to err code : ' + err.code + ' ' + 'message :' +
      err.message);
      return;
    }
    console.info('overlayModuleInfo is ' + JSON.stringify(data));
  });
} catch (err) {
  let code = (err as BusinessError).code;
  let message = (err as BusinessError).message;
  console.error('getTargetOverlayModuleInfosByBundleName failed due to err code : ' + code + ' ' + 'message :' +
    message);
}
```


## getTargetOverlayModuleInfosByBundleName

```TypeScript
function getTargetOverlayModuleInfosByBundleName(targetBundleName: string, moduleName?: string): Promise<Array<OverlayModuleInfo>>
```

获取指定应用中指定module关联的所有OverlayModuleInfo信息。使用promise异步回调。 指定应用是调用方自身时不需要权限。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-overlay-function getTargetOverlayModuleInfosByBundleName(targetBundleName: string, moduleName?: string): Promise<Array<OverlayModuleInfo>>--><!--Device-overlay-function getTargetOverlayModuleInfosByBundleName(targetBundleName: string, moduleName?: string): Promise<Array<OverlayModuleInfo>>-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Overlay

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| targetBundleName | string | 是 |
| moduleName | string | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;OverlayModuleInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [17700002](../errorcode-bundle.md#17700002-指定的modulename不存在) |
| [17700034](../errorcode-bundle.md#17700034-指定的module是overlay特征的module) |
| [17700035](../errorcode-bundle.md#17700035-指定的应用只包含overlay特征的module) |
| [17700001](../errorcode-bundle.md#17700001-指定的bundlename不存在) |

## 示例

```TypeScript
import { overlay } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let targetBundleName = "com.example.myapplication_xxxxx";
let moduleName = "feature";

(async () => {
  try {
    let overlayModuleInfos = await overlay.getTargetOverlayModuleInfosByBundleName(targetBundleName, moduleName);
    console.info('overlayModuleInfos are ' + JSON.stringify(overlayModuleInfos));
  } catch (err) {
    let code = (err as BusinessError).code;
    let message = (err as BusinessError).message;
    console.error('getTargetOverlayModuleInfosByBundleName failed due to err code : ' + code + ' ' + 'message :' +
      message);
  }
})();
```
