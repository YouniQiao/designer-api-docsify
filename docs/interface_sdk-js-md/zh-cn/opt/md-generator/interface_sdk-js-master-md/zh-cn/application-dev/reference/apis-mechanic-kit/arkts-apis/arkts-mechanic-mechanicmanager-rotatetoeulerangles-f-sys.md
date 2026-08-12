# rotateToEulerAngles（系统接口）

## rotateToEulerAngles

```TypeScript
function rotateToEulerAngles(mechId: number, angles: EulerAngles, duration: number): Promise<Result>
```

将机械设备旋转到绝对角度

**起始版本：** 20

<!--Device-mechanicManager-function rotateToEulerAngles(mechId: int, angles: EulerAngles, duration: int): Promise<Result>--><!--Device-mechanicManager-function rotateToEulerAngles(mechId: int, angles: EulerAngles, duration: int): Promise<Result>-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mechId | number | 是 |
| angles | [EulerAngles](arkts-mechanic-mechanicmanager-eulerangles-i-sys.md) | 是 |
| duration | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Result & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300002-设备未连接) |

## 示例

```TypeScript
let degree: mechanicManager.EulerAngles = {
  yaw: 0.9 * Math.PI,
  roll: 0.9 * Math.PI,
  pitch: 0.9 * Math.PI
}
mechanicManager.rotateToEulerAngles(0, degree, 500)
  .then((result: mechanicManager.Result) => {
    console.info(`'Rotate result:' ${result}`);
  });
console.info('End rotation');
```
