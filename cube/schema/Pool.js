cube(`Pool`, {
  sql: `SELECT * FROM test.pool`,

  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started
  },

  joins: {},

  measures: {
    tvl: {
      sql: `tvlusd`,
      type: `runningTotal`,
      format: `currency`,
    },
    apybase: {
      sql: `${CUBE}.\`apyBase\``,
      type: `number`,
    },

    apyreward: {
      sql: `${CUBE}.\`apyReward\``,
      type: `number`,
    },

    apy: {
      sql: `apy`,
      type: `number`,
    },

    apypct1d: {
      sql: `${CUBE}.\`apyPct1D\``,
      type: `number`,
    },

    apypct7d: {
      sql: `${CUBE}.\`apyPct7D\``,
      type: `number`,
    },

    apypct30d: {
      sql: `${CUBE}.\`apyPct30D\``,
      type: `number`,
    },
  },

  dimensions: {
    timeExtracted: {
      sql: `_time_extracted`,
      type: `time`,
    },

    chain: {
      sql: `chain`,
      type: `string`,
    },

    project: {
      sql: `project`,
      type: `string`,
    },

    symbol: {
      sql: `symbol`,
      type: `string`,
    },

    rewardtokens: {
      sql: `${CUBE}.\`rewardTokens\``,
      type: `string`,
    },

    pool: {
      sql: `pool`,
      type: `string`,
      primaryKey: true,
    },

    stablecoin: {
      sql: `stablecoin`,
      type: `string`,
    },

    ilrisk: {
      sql: `${CUBE}.\`ilRisk\``,
      type: `string`,
    },

    exposure: {
      sql: `exposure`,
      type: `string`,
    },

    predictedclass: {
      sql: `${CUBE}.\`predictedClass\``,
      type: `string`,
    },

    predictedprobability: {
      sql: `${CUBE}.\`predictedProbability\``,
      type: `string`,
    },

    binnedconfidence: {
      sql: `${CUBE}.\`binnedConfidence\``,
      type: `string`,
    },

    poolmeta: {
      sql: `${CUBE}.\`poolMeta\``,
      type: `string`,
    },

    mu: {
      sql: `mu`,
      type: `string`,
    },

    sigma: {
      sql: `sigma`,
      type: `string`,
    },

    count: {
      sql: `count`,
      type: `string`,
    },

    outlier: {
      sql: `outlier`,
      type: `string`,
    },

    underlyingtokens: {
      sql: `${CUBE}.\`underlyingTokens\``,
      type: `string`,
    },
  },

  dataSource: `default`,
});
