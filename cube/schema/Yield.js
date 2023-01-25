cube(`Yield`, {
  sql: `SELECT * FROM test.yield`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [id, timestamp]
    }
  },
  
  dimensions: {
    id: {
      sql: `id`,
      type: `string`,
      primaryKey: true
    },
    
    pool: {
      sql: `pool`,
      type: `string`
    },
    
    chain: {
      sql: `chain`,
      type: `string`
    },
    
    project: {
      sql: `project`,
      type: `string`
    },
    
    symbol: {
      sql: `symbol`,
      type: `string`
    },
    
    tvlusd: {
      sql: `${CUBE}.\`tvlUsd\``,
      type: `string`
    },
    
    apy: {
      sql: `apy`,
      type: `string`
    },
    
    apybase: {
      sql: `${CUBE}.\`apyBase\``,
      type: `string`
    },
    
    apyreward: {
      sql: `${CUBE}.\`apyReward\``,
      type: `string`
    },
    
    timestamp: {
      sql: `timestamp`,
      type: `time`
    }
  },
  
  dataSource: `default`
});
