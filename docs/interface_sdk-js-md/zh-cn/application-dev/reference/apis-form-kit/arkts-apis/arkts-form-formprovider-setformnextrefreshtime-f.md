# setFormNextRefreshTime

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## setFormNextRefreshTime

```TypeScript
function setFormNextRefreshTime(formId: string, minute: number, callback: AsyncCallback<void>): void
```

设置指定卡片的下一次刷新时间，使用callback异步回调。适用于需要精确控制卡片刷新时机的场景，例如定时任务等。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| minute | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501002](../errorcode-form.md#16501002-卡片数量达到上限) |
| [16501003](../errorcode-form.md#16501003-无法操作指定卡片) |


## setFormNextRefreshTime

```TypeScript
function setFormNextRefreshTime(formId: string, minute: number): Promise<void>
```

设置指定卡片的下一次刷新时间，使用Promise异步回调。适用于需要精确控制卡片刷新时机的场景，例如定时任务等。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |
| minute | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501002](../errorcode-form.md#16501002-卡片数量达到上限) |
| [16501003](../errorcode-form.md#16501003-无法操作指定卡片) |
