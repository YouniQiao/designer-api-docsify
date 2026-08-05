# NetStatsInfoSequence (System API)

```TypeScript
export type NetStatsInfoSequence = {
    /**
     * Start time for querying traffic.
     *****/
    startTime: int;
    /**
     * End time for querying traffic.
     *****/
    endTime: int;
    /**
     * Detailed information of statistics.
     *****/
    info: NetStatsInfo;
  }[]
```

An \_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ array with start time and end time.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-statistics-export type NetStatsInfoSequence = {    /**     * Start time for querying traffic.     *****/    startTime: int;    /**     * End time for querying traffic.     *****/    endTime: int;    /**     * Detailed information of statistics.     *****/    info: NetStatsInfo;  }[]--><!--Device-statistics-export type NetStatsInfoSequence = {    /**     * Start time for querying traffic.     *****/    startTime: int;    /**     * End time for querying traffic.     *****/    endTime: int;    /**     * Detailed information of statistics.     *****/    info: NetStatsInfo;  }[]-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Property type:** {
    /**
     * Start time for querying traffic.
     * @type { int }
     * @syscap SystemCapability.Communication.NetManager.Core
     * @systemapi Hide this for inner system use.
     * @since 12
     */
    startTime: int;
    /**
     * End time for querying traffic.
     * @type { int }
     * @syscap SystemCapability.Communication.NetManager.Core
     * @systemapi Hide this for inner system use.
     * @since 12
     */
    endTime: int;
    /**
     * Detailed information of statistics.
     * @type { NetStatsInfo }
     * @syscap SystemCapability.Communication.NetManager.Core
     * @systemapi Hide this for inner system use.
     * @since 12
     */
    info: NetStatsInfo;
  }[]

