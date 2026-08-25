# hasMatchedCallLog

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## hasMatchedCallLog

```TypeScript
function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: number): Promise<boolean>
```

检查是否有符合条件的通话记录，默认查询6小时以内的通话记录，仅针对运营商通话。使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.CHECK_CALL_LOG

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| phoneNumber | string | 是 |
| minDuration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16700001](../errorcode-contacts.md#16700001-系统内部错误) |
| [16700002](../errorcode-contacts.md#16700002-参数检查失败) |


## hasMatchedCallLog

```TypeScript
function hasMatchedCallLog(context: Context, phoneNumber: string, minDuration: number, withinTime: number): Promise<boolean>
```

检查是否有符合条件的通话记录，仅针对运营商通话。使用Promise异步回调。

**起始版本：** 24

**需要权限：** ohos.permission.CHECK_CALL_LOG

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| phoneNumber | string | 是 |
| minDuration | number | 是 |
| withinTime | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16700001](../errorcode-contacts.md#16700001-系统内部错误) |
| [16700002](../errorcode-contacts.md#16700002-参数检查失败) |
