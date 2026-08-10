# ScannerSyncDevice

定义扫描仪同步设备的接口。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-scan-interface ScannerSyncDevice--><!--Device-scan-interface ScannerSyncDevice-End-->

**System capability:** SystemCapability.Print.PrintFramework

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## discoveryMode

```TypeScript
discoveryMode: ScannerDiscoveryMode
```

发现模式。

**Type:** [ScannerDiscoveryMode](arkts-basicservices-scan-scannerdiscoverymode-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ScannerSyncDevice-discoveryMode: ScannerDiscoveryMode--><!--Device-ScannerSyncDevice-discoveryMode: ScannerDiscoveryMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## oldScannerId

```TypeScript
oldScannerId?: string
```

旧的扫描仪ID，仅在syncMode为"update"时有效。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ScannerSyncDevice-oldScannerId?: string--><!--Device-ScannerSyncDevice-oldScannerId?: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## scannerId

```TypeScript
scannerId: string
```

扫描仪ID。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ScannerSyncDevice-scannerId: string--><!--Device-ScannerSyncDevice-scannerId: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

## syncMode

```TypeScript
syncMode: ScannerSyncMode
```

同步模式。

**Type:** [ScannerSyncMode](arkts-basicservices-scan-scannersyncmode-e.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ScannerSyncDevice-syncMode: ScannerSyncMode--><!--Device-ScannerSyncDevice-syncMode: ScannerSyncMode-End-->

**System capability:** SystemCapability.Print.PrintFramework

## uniqueId

```TypeScript
uniqueId: string
```

唯一ID。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-ScannerSyncDevice-uniqueId: string--><!--Device-ScannerSyncDevice-uniqueId: string-End-->

**System capability:** SystemCapability.Print.PrintFramework

