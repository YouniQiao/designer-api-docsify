# getFormRect

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## getFormRect

```TypeScript
function getFormRect(formId: string): Promise<formInfo.Rect>
```

查询卡片位置、尺寸，使用Promise异步回调。适用于需要获取卡片在屏幕上的位置和尺寸信息的场景，例如卡片动效、位置校准、布局计算等。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| formId | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;formInfo.Rect & gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [16500060](../errorcode-form.md#16500060-连接服务失败) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16501001](../errorcode-form.md#16501001-卡片id不存在) |
| [16501003](../errorcode-form.md#16501003-无法操作指定卡片) |
