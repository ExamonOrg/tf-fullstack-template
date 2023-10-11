module.exports.handler = async (event, context) => {
  try {
    const response = {
      statusCode: 200,
      body: JSON.stringify({
        message: 'Hi Boss! Reporting for duty!'
      })
    };
    return response;
  } catch (err) {
    console.error(err);
    return {
      statusCode: 500,
      body: JSON.stringify({
        message: 'Internal server error'
      })
    };
  }
};
