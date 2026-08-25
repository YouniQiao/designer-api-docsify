# createFormBindingData

## 导入模块

```TypeScript
import { formBindingData } from 'kits/@kit.FormKit';
```

## createFormBindingData

```TypeScript
function createFormBindingData(obj?: Object | string): FormBindingData
```

创建一个FormBindingData对象。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| obj | Object \| string | 否 |

**返回值：**

| 类型 |
| --- |
| [FormBindingData](arkts-form-formbindingdata-formbindingdata-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
