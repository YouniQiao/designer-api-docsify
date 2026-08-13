# suspend（系统接口）

## suspend

```TypeScript
function suspend(isImmediate?: boolean): void
```

使设备进入睡眠状态。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** 
- API版本19+：ohos.permission.POWER_MANAGER

<!--Device-power-function suspend(isImmediate?: boolean): void--><!--Device-power-function suspend(isImmediate?: boolean): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isImmediate | boolean | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-连接服务失败) |

## 示例

```TypeScript
try {
    power.suspend();
} catch (err) {
    console.error(`Failed to suspend device. Code: ${err.code}, message: ${err.message}`);
}
```
