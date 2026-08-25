# isDefaultApplicationSync

## 导入模块

```TypeScript
import { defaultAppManager } from 'kits/@kit.AbilityKit';
```

## isDefaultApplicationSync

```TypeScript
function isDefaultApplicationSync(type: string): boolean
```

以同步方法根据系统已定义的应用类型或者[UniformDataType](../../apis-arkdata/arkts-apis/arkts-data-uniformtypedescriptor.md)类型判断当前应用是否是该类型的默认 应用，使用boolean形式返回结果。

**起始版本：** 10

**系统能力：** SystemCapability.BundleManager.BundleFramework.DefaultApp

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | string | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
