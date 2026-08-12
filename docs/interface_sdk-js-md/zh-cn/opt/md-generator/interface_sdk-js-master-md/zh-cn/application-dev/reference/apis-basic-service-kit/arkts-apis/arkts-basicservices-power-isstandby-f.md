# isStandby

## isStandby

```TypeScript
function isStandby(): boolean
```

检测当前设备是否进入待机低功耗续航模式。

**起始版本：** 10

<!--Device-power-function isStandby(): boolean--><!--Device-power-function isStandby(): boolean-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [4900101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900101-连接服务失败) |

## 示例

```TypeScript
try {
    let isStandby = power.isStandby();
    console.info('device is in standby: ' + isStandby);
} catch (err) {
    console.error(`Failed to check isStandby. Code: ${err.code}, message: ${err.message}`);
}
```
