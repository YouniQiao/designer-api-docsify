# getCurrentAngles（系统接口）

## getCurrentAngles

```TypeScript
function getCurrentAngles(mechId: number): EulerAngles
```

获取机械设备的当前角度

**起始版本：** 23

**废弃版本：** -1

<!--Device-mechanicManager-function getCurrentAngles(mechId: int): EulerAngles--><!--Device-mechanicManager-function getCurrentAngles(mechId: int): EulerAngles-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mechId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [EulerAngles](arkts-mechanic-mechanicmanager-eulerangles-i-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../errorcode-mechanic.md#33300002-设备未连接) |

## 示例

```TypeScript
console.info('Query current location');
let currentAngles: mechanicManager.EulerAngles = mechanicManager.getCurrentAngles(0);
console.info(`'Query current location, location:' ${currentAngles}`);
```
