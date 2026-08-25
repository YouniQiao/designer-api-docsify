# cancelOverflow

## 导入模块

```TypeScript
import { formProvider } from 'kits/@kit.FormKit';
```

## cancelOverflow

```TypeScript
function cancelOverflow(formId: string): Promise<void>
```

卡片提供方发起取消互动卡片动效请求，只针对[场景动效类型互动卡片](../../../form/arkts-ui-widget-configuration.md#sceneanimationparams标签)生效，使用 Promise异步回调。

> **说明：**&gt;
> 1. 该接口在省电模式场景下不可使用，会报16501000错误码。&gt;
> 2. 当设备热档位进入HOT场景并且没有点击事件的场景下，该接口会报16501000错误码；当热档位进入OVERHEATED时，任何情况下都会报16501000错误码。热档位信息具体可参考
> [热档位信息](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-thermal-thermallevel-e.md)。

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
| Promise & lt;void & gt; |

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
| [16501011](../errorcode-form.md#16501011-卡片不支持调用当前接口) |
