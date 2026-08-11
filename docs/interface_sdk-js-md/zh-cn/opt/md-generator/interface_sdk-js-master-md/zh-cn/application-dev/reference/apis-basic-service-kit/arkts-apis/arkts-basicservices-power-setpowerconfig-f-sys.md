# setPowerConfig（系统接口）

## setPowerConfig

```TypeScript
function setPowerConfig(sceneName: string, value: string): void
```

根据场景名称设置电源配置值。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.POWER_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-power-function setPowerConfig(sceneName: string, value: string): void--><!--Device-power-function setPowerConfig(sceneName: string, value: string): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sceneName | string | 是 |
| value | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [4900601](../../apis-basic-services-kit/errorcode-power.md#4900601-写电源配置值失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [4900400](../../apis-basic-services-kit/errorcode-power.md#4900400-接口入参无效) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-连接服务失败) |

## 示例

```TypeScript
try {
    power.setPowerConfig('scene_name_test', 'value_test');
    console.info('set power config success');
} catch (err) {
    console.error(`Failed to set power config. Code: ${err.code}, message: ${err.message}`);
}
```
