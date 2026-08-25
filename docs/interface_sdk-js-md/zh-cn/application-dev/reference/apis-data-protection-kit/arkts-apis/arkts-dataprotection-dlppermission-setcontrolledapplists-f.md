# setControlledAppLists

## 导入模块

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## setControlledAppLists

```TypeScript
function setControlledAppLists(appLists: Array<string>, userId?: number): Promise<void>
```

设置受企业DLP控制的应用程序列表。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.DLP_POLICY_MANAGER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.DataLossPrevention

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| appLists | Array & lt;string & gt; | 是 |
| userId | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [19100001](../errorcode-dlp.md#19100001-入参错误) |
| [19100011](../errorcode-dlp.md#19100011-系统服务工作异常) |
| [19100023](../errorcode-dlp.md#19100023-指定的用户id与当前用户id不一致) |
| [19100024](../errorcode-dlp.md#19100024-个人空间用户不支持设置受控应用) |
