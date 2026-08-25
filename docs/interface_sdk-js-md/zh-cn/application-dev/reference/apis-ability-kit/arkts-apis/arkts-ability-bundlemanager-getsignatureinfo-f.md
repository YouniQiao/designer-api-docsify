# getSignatureInfo

## 导入模块

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getSignatureInfo

```TypeScript
function getSignatureInfo(uid: number): SignatureInfo
```

根据给定的uid获取对应应用的[签名信息](arkts-ability-bundleinfo-signatureinfo-i.md)。

**起始版本：** 18

**需要权限：** ohos.permission.GET_SIGNATURE_INFO

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
