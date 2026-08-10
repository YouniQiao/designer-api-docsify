# getPowerConfig（系统接口）

## 导入模块

```TypeScript
import { power } from 'kits/@kit.BasicServicesKit';
```

## getPowerConfig

```TypeScript
function getPowerConfig(sceneName: string): string
```

按场景名称查询电源配置值。

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.POWER_CONFIG

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-power-function getPowerConfig(sceneName: string): string--><!--Device-power-function getPowerConfig(sceneName: string): string-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sceneName | string | 是 | 电源配置的场景名称。最大长度128字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回电源配置值。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 4900400 | Invalid parameter. Possible causes: 1. The sceneName parameter is an empty string; 2. The length of sceneName parameter exceeds 128 bytes. |
| 4900101 | Failed to connect to the service. |
| 4900501 | Failed to read the power configuration value. |

## 示例

```TypeScript
try {
    let configVal = power.getPowerConfig('scene_name_test');
    console.info('get power config success, configVal: ' + configVal);
} catch (err) {
    console.error(`Failed to get power config. Code: ${err.code}, message: ${err.message}`);
}
```

