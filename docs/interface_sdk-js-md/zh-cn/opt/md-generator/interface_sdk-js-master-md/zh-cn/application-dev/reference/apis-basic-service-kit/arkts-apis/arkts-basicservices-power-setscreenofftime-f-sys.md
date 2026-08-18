# setScreenOffTime（系统接口）

## 导入模块

```TypeScript
```

## setScreenOffTime

```TypeScript
function setScreenOffTime(timeout: number): void
```

设置熄屏超时时间。

**起始版本：** 23

**需要权限：** 
- API版本19+：ohos.permission.POWER_MANAGER

<!--Device-power-function setScreenOffTime(timeout: long): void--><!--Device-power-function setScreenOffTime(timeout: long): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-连接服务失败) |

**示例**

```TypeScript
try {
    power.setScreenOffTime(30000);
} catch (err) {
    console.error(`Failed to set screen off time. Code: ${err.code}, message: ${err.message}`);
}
```
