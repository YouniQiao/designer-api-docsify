# getShieldStatus（系统接口）

## 导入模块

```TypeScript
import { inputConsumer } from 'kits/@kit.InputKit';
```

## getShieldStatus

```TypeScript
function getShieldStatus(shieldMode: ShieldMode): boolean
```

获取系统快捷键屏蔽类型。

**起始版本：** 11

**需要权限：** ohos.permission.INPUT_CONTROL_DISPATCHING

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shieldMode | [ShieldMode](arkts-input-inputconsumer-shieldmode-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
