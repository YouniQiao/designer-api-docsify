# ServiceInfo (System API)

Represents the cloud service information.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-cloudExtension-export interface ServiceInfo--><!--Device-cloudExtension-export interface ServiceInfo-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## enableCloud

```TypeScript
enableCloud: boolean
```

Whether the cloud service is enabled. The value true means that the cloud service is enabled,and the value false means the opposite.

**Type:** boolean

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ServiceInfo-enableCloud: boolean--><!--Device-ServiceInfo-enableCloud: boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## id

```TypeScript
id: string
```

Cloud account ID generated using SHA-256.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ServiceInfo-id: string--><!--Device-ServiceInfo-id: string-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## remainingSpace

```TypeScript
remainingSpace: long
```

Available account space on the server, in KB.

**Type:** long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ServiceInfo-remainingSpace: long--><!--Device-ServiceInfo-remainingSpace: long-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## totalSpace

```TypeScript
totalSpace: long
```

Total account space on the server, in KB.

**Type:** long

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ServiceInfo-totalSpace: long--><!--Device-ServiceInfo-totalSpace: long-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

## user

```TypeScript
user: int
```

Current user ID of the device.

**Type:** int

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-ServiceInfo-user: int--><!--Device-ServiceInfo-user: int-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Server

**System API:** This is a system API.

