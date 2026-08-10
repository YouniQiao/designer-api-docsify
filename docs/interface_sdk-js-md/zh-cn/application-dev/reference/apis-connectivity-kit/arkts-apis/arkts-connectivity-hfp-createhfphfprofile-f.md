# createHfpHfProfile

## 导入模块

```TypeScript
import { hfp } from 'kits/@kit.ConnectivityKit';
```

## createHfpHfProfile

```TypeScript
function createHfpHfProfile(): HandsFreeHfProfile
```

create the instance of HF(Hands-Free Unit) for HFP(Hands-Free Profile).

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-hfp-function createHfpHfProfile(): HandsFreeHfProfile--><!--Device-hfp-function createHfpHfProfile(): HandsFreeHfProfile-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HandsFreeHfProfile](arkts-connectivity-hfp-handsfreehfprofile-i-sys.md) | Returns the instance of profile. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |

## 示例

```TypeScript
try {
    let hfProfile = hfp.createHfpHfProfile();
    console.info('hf success');
} catch (err) {
    console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
}
```

