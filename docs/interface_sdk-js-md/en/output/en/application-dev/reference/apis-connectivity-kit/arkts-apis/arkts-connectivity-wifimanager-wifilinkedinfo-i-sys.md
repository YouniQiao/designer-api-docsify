# WifiLinkedInfo

Wi-Fi connection information.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-wifiManager-interface WifiLinkedInfo--><!--Device-wifiManager-interface WifiLinkedInfo-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## chload

```TypeScript
chload: int
```

The load value of this Wi-Fi connection. A greater value indicates a higher load.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WifiLinkedInfo-chload: int--><!--Device-WifiLinkedInfo-chload: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## isHiLinkProNetwork

```TypeScript
isHiLinkProNetwork?: boolean
```

Whether the Wi-Fi hotspot is HiLinkPro network.

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-WifiLinkedInfo-isHiLinkProNetwork?: boolean--><!--Device-WifiLinkedInfo-isHiLinkProNetwork?: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## networkId

```TypeScript
networkId: int
```

The ID(uniquely identifies) of a Wi-Fi connection.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WifiLinkedInfo-networkId: int--><!--Device-WifiLinkedInfo-networkId: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## snr

```TypeScript
snr: int
```

The signal-to-noise ratio (SNR) of this Wi-Fi connection.

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WifiLinkedInfo-snr: int--><!--Device-WifiLinkedInfo-snr: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## suppState

```TypeScript
suppState: SuppState
```

The state of the supplicant of this Wi-Fi connection.

**Type:** SuppState

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-WifiLinkedInfo-suppState: SuppState--><!--Device-WifiLinkedInfo-suppState: SuppState-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## wifiTxRxValid

```TypeScript
wifiTxRxValid?: boolean
```

Whether Wi-Fi Tx and Rx are both working properly

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WifiLinkedInfo-wifiTxRxValid?: boolean--><!--Device-WifiLinkedInfo-wifiTxRxValid?: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

