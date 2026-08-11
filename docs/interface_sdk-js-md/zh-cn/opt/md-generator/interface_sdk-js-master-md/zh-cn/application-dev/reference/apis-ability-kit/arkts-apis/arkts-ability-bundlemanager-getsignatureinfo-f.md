# getSignatureInfo

## getSignatureInfo

```TypeScript
function getSignatureInfo(uid: number): SignatureInfo
```

根据给定的uid获取对应应用的[签名信息](arkts-ability-bundlemanager-signatureinfo-t.md)。

**起始版本：** 18

**需要权限：** ohos.permission.GET_SIGNATURE_INFO

<!--Device-bundleManager-function getSignatureInfo(uid: int): SignatureInfo--><!--Device-bundleManager-function getSignatureInfo(uid: int): SignatureInfo-End-->

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | number | 是 |

**返回值：**

| 类型 |
| --- |
| [SignatureInfo](../../apis-mdm-kit/arkts-apis/arkts-mdm-bundlemanager-signatureinfo-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [17700021](../errorcode-bundle.md#17700021-指定的uid无效) |

## 示例

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let uid = 20010005; // uid需要替换为对应应用程序的UID。
try {
  let data = bundleManager.getSignatureInfo(uid);
  hilog.info(0x0000, 'testTag', 'getSignatureInfo successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSignatureInfo failed. Cause: %{public}s', message);
}
```
