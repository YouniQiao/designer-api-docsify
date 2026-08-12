# setPowerKeyFilteringStrategy（系统接口）

## setPowerKeyFilteringStrategy

```TypeScript
function setPowerKeyFilteringStrategy(strategy: PowerKeyFilteringStrategy): void
```

设置电源键过滤策略，在电源服务订阅电源键事件后，用于配置电源键事件的处理方式。

电源键过滤策略见[power.PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md#PowerKeyFilteringStrategy)接口。

**起始版本：** 21

**需要权限：** ohos.permission.POWER_MANAGER

<!--Device-power-function setPowerKeyFilteringStrategy(strategy: PowerKeyFilteringStrategy): void--><!--Device-power-function setPowerKeyFilteringStrategy(strategy: PowerKeyFilteringStrategy): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| strategy | [PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [4900101](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-power.md#4900101-连接服务失败) |

## 示例

```TypeScript
try {
    power.setPowerKeyFilteringStrategy(power.PowerKeyFilteringStrategy.LONG_PRESS_FILTERING_ONCE);
} catch (err) {
    console.error(`Failed to set power key filtering strategy. Code: ${err.code}, message: ${err.message}`);
}
```
