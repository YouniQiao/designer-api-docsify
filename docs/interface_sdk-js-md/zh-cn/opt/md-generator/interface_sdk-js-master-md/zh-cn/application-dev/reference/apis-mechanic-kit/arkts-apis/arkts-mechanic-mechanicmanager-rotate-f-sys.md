# rotate（系统接口）

## rotate

```TypeScript
function rotate(mechId: number, angles: RotationAngles, duration: number): Promise<Result>
```

将机械设备旋转到相对角度

**起始版本：** 23

**废弃版本：** -1

<!--Device-mechanicManager-function rotate(mechId: int, angles: RotationAngles, duration: int): Promise<Result>--><!--Device-mechanicManager-function rotate(mechId: int, angles: RotationAngles, duration: int): Promise<Result>-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mechId | number | 是 |
| angles | [RotationAngles](arkts-mechanic-mechanicmanager-rotationangles-i-sys.md) | 是 |
| duration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../errorcode-mechanic.md#33300002-设备未连接) |

## 示例

```TypeScript
console.info('Start rotate');
let degree: mechanicManager.RotationAngles = {
  yaw: 0.1 * Math.PI,
  roll: 0.0,
  pitch: 0.0
}
mechanicManager.rotate(0, degree, 500)
  .then((result: mechanicManager.Result) => {
    console.info(`'Rotate result:' ${result}`);
  });
console.info('End rotation');
```
