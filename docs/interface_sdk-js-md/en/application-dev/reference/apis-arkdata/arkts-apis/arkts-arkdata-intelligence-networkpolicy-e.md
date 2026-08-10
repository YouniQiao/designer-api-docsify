# NetworkPolicy

下载云侧模型的网络策略枚举。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-intelligence-enum NetworkPolicy--><!--Device-intelligence-enum NetworkPolicy-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## WIFI_ONLY

```TypeScript
WIFI_ONLY = 0
```

仅在Wi-Fi状态下下载模型，适用于需要节省移动数据流量的场景。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NetworkPolicy-WIFI_ONLY = 0--><!--Device-NetworkPolicy-WIFI_ONLY = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

## WIFI_AND_CELLULAR

```TypeScript
WIFI_AND_CELLULAR = 1
```

在Wi-Fi和蜂窝网络状态下下载模型，适用于需要快速获取模型且允许使用移动数据的场景。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NetworkPolicy-WIFI_AND_CELLULAR = 1--><!--Device-NetworkPolicy-WIFI_AND_CELLULAR = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.DataIntelligence.Core

