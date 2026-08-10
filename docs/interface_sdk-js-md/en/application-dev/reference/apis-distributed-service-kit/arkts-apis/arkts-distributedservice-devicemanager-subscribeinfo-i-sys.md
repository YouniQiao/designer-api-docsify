# SubscribeInfo (System API)

发现信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-deviceManager-interface SubscribeInfo--><!--Device-deviceManager-interface SubscribeInfo-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { deviceManager } from 'kits/@kit.DistributedServiceKit';
```

## capability

```TypeScript
capability: SubscribeCap
```

发现能力。

**Type:** [SubscribeCap](arkts-distributedservice-devicemanager-subscribecap-e-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-SubscribeInfo-capability: SubscribeCap--><!--Device-SubscribeInfo-capability: SubscribeCap-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## freq

```TypeScript
freq: ExchangeFreq
```

发现频率。

**Type:** [ExchangeFreq](arkts-distributedservice-devicemanager-exchangefreq-e-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-SubscribeInfo-freq: ExchangeFreq--><!--Device-SubscribeInfo-freq: ExchangeFreq-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## isSameAccount

```TypeScript
isSameAccount: boolean
```

是否同账号，true表示同账号，false表示异账号。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-SubscribeInfo-isSameAccount: boolean--><!--Device-SubscribeInfo-isSameAccount: boolean-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## isWakeRemote

```TypeScript
isWakeRemote: boolean
```

是否唤醒设备，true表示唤醒，false表示不用唤醒。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-SubscribeInfo-isWakeRemote: boolean--><!--Device-SubscribeInfo-isWakeRemote: boolean-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## medium

```TypeScript
medium: ExchangeMedium
```

发现类型。

**Type:** [ExchangeMedium](arkts-distributedservice-devicemanager-exchangemedium-e-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-SubscribeInfo-medium: ExchangeMedium--><!--Device-SubscribeInfo-medium: ExchangeMedium-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## mode

```TypeScript
mode: DiscoverMode
```

发现模式。

**Type:** [DiscoverMode](arkts-distributedservice-devicemanager-discovermode-e-sys.md)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-SubscribeInfo-mode: DiscoverMode--><!--Device-SubscribeInfo-mode: DiscoverMode-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

## subscribeId

```TypeScript
subscribeId: number
```

发现标识，用于标识不同的发现周期。 取值范围1~65535。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 11

<!--Device-SubscribeInfo-subscribeId: number--><!--Device-SubscribeInfo-subscribeId: number-End-->

**System capability:** SystemCapability.DistributedHardware.DeviceManager

**System API:** This is a system API.

